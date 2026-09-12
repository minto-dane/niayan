# Nia OS — AIエージェントへの引き継ぎ

**Debian 13 KDE開発ISOは起動・導入のVM受入済み。本番・実機は未認定。**
実ISOの対象hashと6項目の受入は`distribution/evidence/debian13/accepted-09/README.ja.md`。BIOS/UEFI/Secure Boot、実日本語入力、オフライン／オンライン導入と再起動、通常ミラーの署名付きAPT索引取得を確認した。ISO 09/10の実バイト列一致、対応ソース1,415組・4,667ファイルの収集・Linux本体補完・コピー後の照合も完了した。`distribution/release/`のソース補完はイメージ構築とは別工程で、内蔵カーネルの本体を省略しない。未接続の独自機能まで完成扱いにしない。
既存コンポーネントの基準実行では、固定コンテナでの全実コンパイル・58 Ada main・555 Python試験・18バイナリ再現性・独立ビルドと、全7repoの厳格なflow/proveを通過した。対象source subjectと証明範囲はSTATUSと実行証跡で確認する。Python試験や模擬D-Busの成功を形式証明・実デスクトップ試験に置き換えないでください。

## 固定した製品方針
2026-09-08の最新指示は、Debian 13 Trixieを維持しながらAPT/dpkgを完全置換し、Niaを唯一のパッケージ管理主体にすること。Ubuntu・Kicksecure・公的ハードニング資料を参照し、操作性を維持する。現在のISO 09は旧APT経路の比較基準であり、完全置換は未完。最新判断は`distribution/docs/decisions/0002-native-package-authority.ja.md`、移行工程は`distribution/native/`、セキュリティ基準は`distribution/hardening/`。開発Distrobox/ビルダーのAPT使用は稼働NiaOSの管理主体と別。依存削除・偽Provides・常時成功callback・任意scriptのhost root実行で完成にしない。上流ソースへ独自パッチを当てず、7コンポーネントのAPI・永続形式・検査を強引に変更しない。7リポジトリは独立維持する。旧Forky供給lockや独自UKI等の未受入機能をTrixieで検証済みとしない。

## 最初に読むもの

最新の管理インターフェース判断は`distribution/docs/decisions/0003-management-interface.ja.md`。
Niaが所有する管理機能はinstallp等の採用コマンド体系だけを公開し、公開nia/niactl等の
代替入口を作らない。内部SDKとworkerは別。systemd等の独立した外部工具は元のコマンドを
維持し、互換ラッパーを作らない。emgr/epkgのnative緊急修正を同じcatalog/writerへ接続する
設計変更は許可済み。自作コードと説明は中立名称を使い、原本メタデータ・ライセンス・
hash付き過去証跡は改変しない。現在の12入口のうちepkgのテンプレート作成とemgrの
成果物表示、emgr_download_ifixの署名付きHTTPS取得は動作する。
inutocの媒体索引とinstallp/geninstallの媒体一覧も実装した。詳細はdistribution/native/media.ja.md。
供給認証は上流TUFを使用し、信頼cacheを一つの原子的checkpointとして保存する。
詳細はdistribution/native/repository.ja.md。
本番の鍵・policy配備と独立trust floor、契約の意味検証は未完。稼働管理器への接続・対話作成・応答互換性の受入は未完。
多言語インターフェイスはdistribution/docs/decisions/0004-localized-interface.ja.mdに従う。
gettextの実行別UIを使い、操作・署名・catalogと表示言語を分離する。英語原文119件と
日本語・独・西・仏・韓・中国語簡体字・繁体字の7翻訳catalogを実装済み。
第三者訳文レビューは未実施。製品の対象はDebian 13の全言語。distribution/native/debian-languages.jsonの全509 locale組と
installer 78選択肢を扱い、英語fallbackを翻訳完了と数えない。i18n-release-checkは
全言語翻訳が完了するまで失敗を維持する。TUI/GUIとRTL・幅・アクセシビリティは未受入。
追加調査と各コマンドの採用境界は`distribution/native/command-review.ja.md`を参照。

`STATUS.ja.md` → `capsulecore/docs/consent.ja.md` → `assurance/docs/engineering/specs/production-closure.ja.md`。
実行結果はsource hashに束縛した`assurance/evidence/engineering-*/report.json`等。`consent-integration`は取り込み時の履歴。旧evidenceを現行のPASSとして引用しない。

## 次の作業順

2026-09-12の追加必須条件: C等の低水準コードは形式検証と航空宇宙の厳格なコード基準を要求する。
C以外にも影響に応じた基準を適用する。規範はassurance/docs/engineering/specs/implementation-assurance.ja.md。
通常試験/ASanの成功を形式証明とせず、SPARK対象外Ada、FFI、特権Python、シェル/配布/CIを含める。
既存C全体の形式検証・規則適合は未完。本番条件を緩めたり言語変更で回避しない。
小さい関数の証明をOS操作・外部ライブラリ・全実装の証明へ拡大解釈しない。工具不在/unknown/timeoutは未達。
証明harness、環境仮定、実ソースのhashと全未証明条件を保持し、リソース制限を維持する。

2026-09-10の最新指示: 着手済みの共有参照改善の比較・回帰確認を終えたら、本番デプロイを
妨げる未実装部分に集中する。追加の性能研究、試験器の拡張、同じ入力の再検証だけを主作業にしない。
試験は変更境界とリリース判定に必要な範囲へ絞り、検証済みで入力不変の工程は繰り返さない。
以下の一般的な検査手順より、この利用者の最新方針を優先する。
優先対象は実DEBの所有権・全効果とroot組立て、本番認可/供給provider、管理コマンドと実サービスの
接続、起動切替と復旧、完全置換ISOである。全言語翻訳等の既存製品要件も取り消されていない。
SDKと人工fixtureの成功を製品接続完了にしない。

2026-09-12 UTC追補。root handoffの特権Pythonを厳格型検査と明示的な有限制御へ移行した。
ADR-0119、REQ-157/HAZ-143/FAULT-156。受信/応答試行をI/O前に記録し、失敗/閉鎖後の再利用を拒否する。
FD解放のOSErrorで残るFD/pidfd/socket解放が止まる経路を修正した。所有参照を取り外して一度だけcloseし、
同じ番号の再試行を避ける。入力解放失敗後に成功応答を送らない。整数boottimeと有限poll予算も導入した。

固定containerで10項目の制御/障害試験と、実root/非root・pidfd・SCM・Ada往復15項目が成功した。
自分のFDを実closeした後のEIO注入と番号再利用を使い、別FDの誤解放と解放漏れを検査した。
媒体/kernel故障や任意非同期中断の完全な検査ではない。実transition関数に独立履歴を組み合わせ、
全到達15構成・29許可辺・76拒否辺を探索した。2つの負の対照を検出し、assert無効化も拒否する。
深さ上限はないが、対象は有限制御/履歴だけ。Python/OS/I/O/全FD寿命の形式証明へ拡大しない。
mypy 1.15.0-5 strict/Any/到達不能制約でruntimeと検査器の2ファイルが成功した。
C/Adaの425入力は不変で、前回の実行物をhash照合して再利用した。今回再compile/ASanとは数えない。

dev/Containerfileと固定snapshotからCBMC/mypy入り開発imageを実構築した。
imageはsha256:76d5c00dfa833ce7ae67a192c5663d9bcd5c4104153f5933431dae88c097918c。
約257秒、最小空き4,004,278,272 byte。3 GiB/swap0/CPU1/pids128、空き3 GiB/900秒の停止条件を維持した。
新imageでnetworkなし非rootの型/有限制御検査と、限定wire関数のCBMC208条件が成功した。
全工具package版と入力を保持した。remote CI、全suite、新ISOの構築/実起動は今回実行していない。

subjectはce4255b5980cd2c280046757074c693e983ebbd211b8ac006d707037cc483ec8。
構造/参照/lint/license/生成CIも成功。証跡distribution/evidence/native-transition/handoff-lifecycle-01/（45 file、SHA256SUMS込み）。
全job終了、今回VM作成/ストレージ削除/公開は行っていない。私有labはroot-handoff-lifecycle-01。
新imageはnew-dev-image.id、旧受入imageはdev-image.idで区別する。
次は新基準へ残る重要runtimeを適合させ、本番の現在供給/世代admission、正確な同意、
root session/独立観測と物理遮断を非root世代SDKへ接続する。handoff単体の成功を製品接続完了としない。
C全体の厳格規則/形式検証、全writer排他、bank slot/保持/GC、実root/boot切替・復旧、
全DEB効果、完全置換ISO、全言語翻訳は未完。既存minto-dane/niaosは別projectなので上書きしない。
本番認定は行っていない。

過去工程の詳しい記録はSTATUS.ja.mdに保持する。ここには現在の境界と作業規則だけを置く。

過去の数値とsource別証跡はSTATUS.ja.mdとdistribution/evidence/native-transition/へ保持する。
以下の既存境界を保つ。

- Catalogは既存NIACSEL1の正規CAS原本であり、Loadは全元DEB/control/payloadを再観測する。
  最終集合receipt、通常更新delta、供給認証、同意、実行phase、所有権、保持閉包は別の検査である。
- 通常更新ではEssential/Protectedのidentity・flag消失を拒否し、検証済みの保護移行経路が別途必要。
  Provides/Replacesを保護identity保持や包括的な上書き権限にしない。
- Payload/indexは全属性と全owner claimを保持するが、実効所有権を選んでいない。
  global PAX、sparse、採用外ACL方言は未対応として拒否する。既存世代v1のfile planへ
  hardlink・全permission bit・負/小数時刻等を切り捨てて渡さず、版付き実行形式で対応する。
- EROFS直接tar入力の固定1.8.6-1実験はACL欠落・時刻不一致等で未採用。
  `/home/nia/devbox/niaos/.work/native-generation-image-01/`には論理2TiBの失敗疎ファイルがある。
  サイズ確認なしの再帰コピー・全hash・圧縮は禁止。以前の展開しかけた部分コピーは削除済み。
- 元DEB SDKは読取/候補構築経路であり、UID0拒否を解除して稼働OSへ転用しない。
  Pythonのtrigger参照状態や媒体/TUF cacheは第二の導入済みDBではない。
  observe_success等を本番の成功callbackとして用いない。
- 論理世代公開の正本はroot.stateのaccepted planとCAS descriptor。generation.nextは作業ファイル。
  Active要求があれば不確定として扱い、欠けたlock/journal/CASを再初期化して正常にしない。

0. 2026-09-08に並列GNATproveで開発PCが高負荷となり、利用者が強制再起動した。重い検証を重ねない。このDistroboxでは`dev/run-limited.sh command ...`の一時user scopeでメモリ3 GiB・swapなし・CPU 1コア分・128プロセスのkernel制限を適用する。flow/proveと選択unit診断はさらに各repoの`ci/proof-guard.py`経由で1件ずつ実行する。制限による失敗を理由に上限を増やす・guardを迂回する・生のGNATproveで再実行することは禁止。制限と残る範囲はADR-0054。通常ビルドも既定JOBS=1を使う。
1. コンポーネント変更は`dev/README.ja.md`に従い固定環境で`make check private-dbus reproducible proof`。配布レシピの変更は`distribution/image/README.ja.md`に従い、`image-check`、影響するDEB/ISOの構築とVM受入を実行する。数学的入力が不変なら同じ証明を重複実行しない。変更時は新しい未証明条件を修正し、証跡を最新の実行入力へ束縛する。既に成功した証拠を更新後の異なる入力へ流用しない。
2. 最新依頼ではパッケージ管理の完全置換とハードニングを優先。native/READMEの未完経路を実装し、新規ISOで更新・障害復旧を受入する。Capsule起動器のpidfd/cgroup/LSM本人確認と`Capsule_Consent_Channel`→Engine→Store→Access_UIも別の未完として維持。SDKの外部関数を「常にTrue/OK」で埋めない。
3. 各資源のnative portal/brokerを実接続。Portalが資源を渡す前にintentを保存。返された資源をユーザー同意と正確に結び付け、取消・失効を実際の遮断まで試験。
4. 研究モデルのroot bootstrap/catalog-WAL、独自DEB意味層、独立復旧起動、独自署名鍵、遠隔HA/fencing、DB復元、独立trust anchor、安全なGCは別の未完として維持する。Debian InstallerのVM受入済みという事実と混同しない。Debian経路の実機・公開運用の確認は別途行う。

## 守る境界
アクセス失敗の監視を権限昇格にしない。生のhost HOME/bus/devicesを公開しない。署名、UI同意、診断、原本の再構成はいずれも単独では実行許可でない。結果不明を未実行にせず、履歴欠落を空の正常状態にしない。revocation完了には資源遮断の観測が必要。コアが疑わしい時は独立rescueへ移る。

## 検査・引き継ぎ
`python3 assurance/ci/engineering.py check`、`lint`、`run-engineering-checks.py --mode source`。
私有D-Busプローブは`capsulecore/ci/test-consent.sh`（専用private D-Bus、実UIなし）。
変更時はADR・要求・危険・故障・テスト台帳、code inventoryを更新。固定vendorは手編集せず確認付き工具を使う。秘密鍵をZIPへ入れない。未実装は未実装と記録し、完全性を宣言するために検査を弱めない。
