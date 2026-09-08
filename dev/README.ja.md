# 再現可能な開発環境

このworkspaceは7コンポーネントとdistributionのGit commitをsubmoduleで固定する。各コンポーネントは兄弟repoがなくても通常のビルド・Ada試験が可能。台帳・profile・共有vendor・Python参照試験の統合検査には全submoduleが必要。

## Distrobox

Debian 13 amd64でworkspace直下から`make bootstrap`を実行する。これは`dev/packages.txt`の依存だけをaptで導入し、Distroboxのapt供給元は変更しない。日常作業と試験は非rootで行う。ホスト側のCLI・共有ライブラリの版は変化しうるため、再現性の基準には次の固定コンテナを使う。

```sh
make build
make check
make private-dbus
make toolchain
make proof
```

`make check`は全Adaソースのコンパイル、18本のアプリケーションのリンク、全登録Ada試験、Python参照試験、固定契約と文書台帳検査を実行する。read-only host observerを含む。root拒否試験は別context、私有D-Bus試験は`make private-dbus`で実行する。実GTK/KDE表示、実サービス変更、ディストリビューション起動は含まない。

## 固定コンテナ

`dev/Containerfile`はDebian 13.6 amd64のimage digestと2026-09-07の署名済みDebian snapshotを固定する。過去snapshotの有効期限だけを無効化し、署名検証は維持する。image構築時にネットワークを使用し、コンポーネントのbuild/test時は無効化できる。

```sh
podman build -f dev/Containerfile -t niaos-dev .
podman run --rm --network=none --userns=keep-id \
  -e HOME=/tmp -v "$PWD:/workspace" niaos-dev make check private-dbus
podman run --rm --network=none --userns=keep-id \
  -e HOME=/tmp -v "$PWD:/workspace" niaos-dev make reproducible
```

Dockerなら`--userns=keep-id`を`--user "$(id -u):$(id -g)"`に置き換える。実行時にprivilegedやhost bus/deviceの共有は不要。Distrobox内で入れ子のrootlessコンテナが許可されない場合はホスト側でこのコマンドを実行できる。

`make reproducible`は異なる長さの2つの新規作業パスで、入力mtime・並列数・タイムゾーンも変えて全アプリケーションを作り、配布台帳にある実行ファイルのSHA-256を比較する。SOURCE_DATE_EPOCHは1788739200。ソースパスは`/usr/src/niaos/<repo>/`へ写像し、変動するコンパイラ一時ファイル引数をDWARF producer情報へ含めない。デバッグ行情報と実行時検査は維持する。コンパイラ設定変更時は`gprbuild -s`で再コンパイルする。異なるCPU/コンパイラ/libc間の同一性を主張する試験ではない。

## GNATprove

正本lockは`assurance/ci/gnatprove.lock.json`。公式配布archiveのSHA-256を確認して非特権cacheへ展開する。各コンポーネントのコピーは生成物。

```sh
python3 assurance/ci/install-gnatprove.py
# 既に取得済みのarchiveをネットワークなしで検証する場合
python3 assurance/ci/install-gnatprove.py --archive /absolute/path/gnatprove.tar.gz
make proof GNATPROVE=/absolute/path/to/bin/gnatprove
```

flow成功は完全な形式証明ではない。`make proof`は警告・未証明を失敗にする。SPARK_Mode=>OffのFFI・Linux境界は別の実行試験とレビューが必要。実行結果は`assurance/evidence/engineering-*/report.json`、再現性結果は`assurance/evidence/reproducibility-*/report.json`にsource subject付きで保存される。これらの生成ディレクトリは通常Gitから除外される。公開する証跡は対象source hashとともに選別して保存する。

## 正本の更新

共有src/runtimeはassuranceだけを編集する。vendorを直接編集しない。変更後に以下を実行し、diffを確認する。

```sh
make rebind
python3 assurance/ci/refresh-lineage.py --write --acknowledge-source-change \
  --adr ADR-0053 --reason '変更の具体的な理由'
make generated
make source-check
make check
```

ADR-0053は初回コンパイル修正の判断であり、将来の別設計変更には新しいADRを追加する。lineage工具は過去のdigestを変更せず、現在の後継を記録する。再生成する署名fixtureの鍵は公開された人工試験専用である。
