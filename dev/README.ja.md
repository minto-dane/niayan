# 再現可能な開発環境

このworkspaceは7コンポーネントとdistributionのGit commitをsubmoduleで固定する。各コンポーネントは兄弟repoがなくても通常のビルド・Ada試験が可能。台帳・profile・共有vendor・Python参照試験の統合検査には全submoduleが必要。

実装には[言語と影響に応じた必須検証基準](../assurance/docs/engineering/specs/implementation-assurance.ja.md)を適用する。
`make proof`はSPARK対象範囲の検証であり、C・FFI・特権Python全体の証明ではない。
`sh dev/run-limited.sh make c-proof CBMC=/absolute/path/cbmc C_PROOF_OUTPUT=/new/output/directory`は、
実192-byte handoff要求検査と到達する純粋helperをCBMCで検証する。全transportの証明ではない。
Debian amd64のcbmc 6.6.0-4実行物をSHA-256で固定し、工具不在・別版・未証明・警告・入力変更で失敗する。
必要な工具DEBは`cbmc_6.6.0-4_amd64.deb`、SHA-256は
02560859a17049c976961c232c4fc58f0747b57f9b751a466b1f368a438b0e41。
Debian依存を備えた隔離環境で取得・照合して使用し、既存検証のために工具制限を回避しない。
出力先は新規directoryに限定し、過去の証跡を上書きしない。現在のC全体は新基準に未適合である。

## Distrobox

Debian 13 amd64でworkspace直下から`make bootstrap`を実行する。これは`dev/packages.txt`の依存だけをaptで導入し、Distroboxのapt供給元は変更しない。日常作業と試験は非rootで行う。ホスト側のCLI・共有ライブラリの版は変化しうるため、再現性の基準には次の固定コンテナを使う。

```sh
sh dev/run-limited.sh make build
sh dev/run-limited.sh make check
sh dev/run-limited.sh make private-dbus
make toolchain
sh dev/run-limited.sh make proof
```

`make check`は全Adaソースのコンパイル、18本のアプリケーションのリンク、全登録Ada試験、Python参照試験、固定契約と文書台帳検査を実行する。read-only host observerを含む。root拒否試験は別context、私有D-Bus試験は`make private-dbus`で実行する。実GTK/KDE表示、実サービス変更、ディストリビューション起動は含まない。署名付きDEB人工fixtureに必要なGPG・agent・gpgv・gpgconf・dpkg-debは必須依存とし、不足時は統合検査を開始前に失敗させる。

`run-limited.sh`はユーザーのsystemdへ一時scopeを作り、全子孫を合計してメモリ3 GiB・swapなし・CPU 1コア分・最大128プロセスへ制限する。このDistroboxでは実際のkernel設定値を読み戻して確認した。既存serviceの設定変更や恒久設定は行わない。ユーザーbusや対応controllerがない場合は失敗し、制限なしで再試行しない。固定コンテナではコンテナ自体の同等の制限を利用する。

## 固定コンテナ

`dev/Containerfile`はDebian 13.6 amd64のimage digestと2026-09-07の署名済みDebian snapshotを固定する。過去snapshotの有効期限だけを無効化し、署名検証は維持する。image構築時にネットワークを使用し、コンポーネントのbuild/test時は無効化できる。

```sh
sh dev/run-limited.sh podman build -f dev/Containerfile -t niaos-dev .
podman run --rm --network=none --userns=keep-id \
  --memory=3g --memory-swap=3g --cpus=1 --pids-limit=128 \
  -e HOME=/tmp -v "$PWD:/workspace" niaos-dev make check private-dbus
podman run --rm --network=none --userns=keep-id \
  --memory=3g --memory-swap=3g --cpus=1 --pids-limit=128 \
  -e HOME=/tmp -v "$PWD:/workspace" niaos-dev make reproducible
```

Dockerなら`--userns=keep-id`を`--user "$(id -u):$(id -g)"`に置き換える。実行時にprivilegedやhost bus/deviceの共有は不要。Distrobox内で入れ子のrootlessコンテナが許可されない場合はホスト側でこのコマンドを実行できる。

通常の非root試験で省略されるroot拒否試験は、専用コンテナ内で実行する。GitHub Actionsも同じ試験を別stepで実行し、終了値とログを保存する。

```sh
podman run --rm --network=none --user 0:0 \
  --memory=3g --memory-swap=3g --cpus=1 --pids-limit=128 \
  -e HOME=/tmp -v "$PWD:/workspace" niaos-dev sh -ec \
  'cd resolvercore/tests; python3 -B -m unittest test_resolution_reference.ToolTests.test_unprivileged_helpers_refuse_root -v'
```

`make reproducible`は異なる長さの2つの新規作業パスで、入力mtime・並列数・タイムゾーンも変えて全アプリケーションを作り、配布台帳にある実行ファイルのSHA-256を比較する。SOURCE_DATE_EPOCHは1788739200。ソースパスは`/usr/src/niaos/<repo>/`へ写像し、変動するコンパイラ一時ファイル引数をDWARF producer情報へ含めない。デバッグ行情報と実行時検査は維持する。コンパイラ設定変更時の再コンパイルには`gprbuild -s`を使う。ただし固定`SOURCE_DATE_EPOCH`下の診断では、再コンパイル後も既存の実行ファイルが再リンクされない挙動を観測した。qualificationと再現性試験は必ず`build`を含まない新規ソースコピーから始め、増分ビルドの終了値だけで更新済みバイナリと判断しない。異なるCPU/コンパイラ/libc間の同一性を主張する試験ではない。

## GNATprove

正本lockは`assurance/ci/gnatprove.lock.json`。公式配布archiveのSHA-256を確認して非特権cacheへ展開する。各コンポーネントのコピーは生成物。

```sh
python3 assurance/ci/install-gnatprove.py
# 既に取得済みのarchiveをネットワークなしで検証する場合
python3 assurance/ci/install-gnatprove.py --archive /absolute/path/gnatprove.tar.gz
sh dev/run-limited.sh make proof GNATPROVE=/absolute/path/to/bin/gnatprove
```

flow成功は完全な形式証明ではない。`make proof`は警告・未証明を失敗にする。SPARK_Mode=>OffのFFI・Linux境界は別の実行試験とレビューが必要。実行結果は`assurance/evidence/engineering-*/report.json`、再現性結果は`assurance/evidence/reproducibility-*/report.json`にsource subject付きで保存される。これらの生成ディレクトリは通常Gitから除外される。公開する証跡は対象source hashとともに選別して保存する。

2026-09-08の高負荷・強制再起動を受け、証明は各repoの`ci/proof-guard.py`経由に統一した。GNATwhy3を含む各プロセスの仮想アドレス空間を1536 MiBに制限し、並列数1、同一UID・同じ`/tmp`内の重複起動拒否、低いCPU優先度、実時間3600秒の上限を適用する。起動時に4096 MiB以上のMemAvailableを要求し、実行中は合計RSS 2048 MiB超過またはMemAvailable 2048 MiB未満で停止する。失敗後の自動再試行・上限引上げは行わない。通常ビルドも既定`JOBS=1`。

選択unitの診断にも同じguardを使う。`-j`は指定しない。診断の成功を全体の受入結果にしない。

```sh
# 対象コンポーネント内で実行。proverの絶対パスを指定する。
sh ../dev/run-limited.sh python3 ci/proof-guard.py --seconds 600 -- /absolute/path/to/bin/gnatprove \
  -P proof.gpr --subdirs=diagnostic -u unit.adb --mode=all \
  --level=1 --timeout=2 --checks-as-errors=on --warnings=error
```

guardの合計RSS監視とniceだけではkernelの総量・CPU quota制限にならないため、前述のscopeまたはコンテナの制限も併用する。[Podmanの資源設定](https://docs.podman.io/en/latest/markdown/podman-run.1.html#memory-m-number-unit)を参照。Distrobox内からの直接のPodman cgroup設定は失敗したが、ユーザーscopeの制限は適用できた。別UIDや別の`/tmp`名前空間を持つコンテナはロックを共有しないため、PC上の重い検証は1件ずつ実行する。背景と制約は[ADR-0054](../assurance/docs/engineering/adr/ADR-0054.ja.md)。

## 特権Pythonの限定検証

`make -C distribution handoff-check`はroot handoffとその有限制御検査器に対して
固定mypy 1.15.0-5のstrict/Any制約を適用し、実transition関数の全到達状態を検査する。
`distribution/native/handoff-mypy.ini`で対象と条件を明示する。通常のnative-checkからも呼ぶ。
失敗/閉鎖後の再利用、受信と応答の順序/回数を扱い、全Python/OS/FD実装の証明とはしない。
詳細と未達条件はADR-0119。依存はdev/packages.txtと生成した各component CIで固定する。

## 正本の更新

共有src/runtimeはassuranceだけを編集する。vendorを直接編集しない。変更後に以下を実行し、diffを確認する。

```sh
make rebind
python3 assurance/ci/refresh-lineage.py --write --acknowledge-source-change \
  --adr ADR-0053 --reason '変更の具体的な理由'
make generated
sh dev/run-limited.sh make source-check
sh dev/run-limited.sh make check
```

ADR-0053は初回コンパイル修正の判断であり、将来の別設計変更には新しいADRを追加する。lineage工具は過去のdigestを変更せず、現在の後継を記録する。再生成する署名fixtureの鍵は公開された人工試験専用である。
