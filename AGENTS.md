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
元DEBのar envelopeと圧縮メンバーを既存CASへ束縛するnative読取SDKを追加した。
原本の全hash・header・順序・サイズを再検査し、保存前に呼出側の全envelopeを照合する。
固定環境でpkgcore全ソース・4アプリ・15 Ada main、新読取器764 assertionsが成功した。
二つの入口のroot拒否と実DEB 7個・全21メンバーの独立ar/CAS照合も成功した。
別パス・入力mtime・TZの新規ビルドで19実行ファイルが一致し、346入力hashを照合した。
ソース24工程の前後subjectは`a1fea042e264bffca34da1d85cac7fea9f495061edd22633009bdbcb72a37945`で一致した。
全7repoのproof入力は不変で、新runtimeはSPARK証明の対象外。
詳細はdistribution/native/deb-container.ja.mdと
distribution/evidence/native-transition/deb-container-01/README.ja.md。
圧縮tar/control・全効果・稼働catalog・実root/boot・完全置換ISOは未完である。

遅延トリガーの参照状態を`distribution/tools/debian_trigger_state.py`へ追加した。ADR-0059。
処理中と未処理を分け、再発火を保持し、受信者自身の待機が解消してから待機解除を伝播する。
scope/開始revision/受信者/名前からattemptを作り、古い応答と異なるcheckpointを拒否する。
observe_successは別途検証した観測を与えた場合の参照遷移で、認証APIやhandler起動器ではない。
既存CAS/WALに接続済みと誤認せず、Pythonの第二の導入済みDBを作らない。
固定環境の配布工具158件（参照状態13件を含む）とソース24工程が成功。証跡は
`distribution/evidence/native-transition/trigger-state-01/`、subjectは
`30d4b667646dad5a8732fec8a78c109b634d7e319c08680a67834d5b832938d2`。
通常構成・失敗・remove/purge・interest寿命、観測認証とnative実行、実電源断は未完。

直近で`distribution/native/media.py`を追加し、inutocとinstallp/geninstallの媒体操作を接続した。
元DEBから有界に索引を作り、毎回再検査する。directory fd/flock、原本と索引の前後確認、
一時索引のfsync/renameを使う。媒体キャッシュは署名認証でも導入済みDBでもない。
設計はADR-0058。142試験（媒体14件を含む）、保存済み7実DEBの公開コマンド試験、ソース24工程が成功。
証跡は`distribution/evidence/management-interface/media-01/`、source subjectは
`b2b9795aa6de090627c3e742be5dfabc9f408015a5430394dea3e0d871200f53`。
全7repoのproof入力は不変。完全な応答互換性、稼働catalog・全効果・boot・新ISOは未完。

最新の担当境界は`distribution/native/ownership.ja.md`。内部dpkgバックエンドも採用しない。
`distribution/tools/debian_triggers.py`で6種の宣言と段階・ファイル変更の発火先、
await関係を計算し、原本DEBの観測と候補catalogへ宣言を保持した。ADR-0057。
別の導入済みDBや特権Python実行器は作っていない。nativeのpending状態、handler再発火、
WAL・取消・再開は未接続で、候補catalogの効果完了flagは成立しない。
追加翻訳とともに固定コンテナの128件と配布工具145件、ソース24工程が成功した。
原本triggers 1,186ファイルのhash・サイズ照合と解析も成功した。今回の証跡は
`distribution/evidence/native-transition/triggers-localization-01/`、subjectは
`ef6012e2bbd64da55bc9b012abc15e80acb5b4b9d83564c0d32e36d836365fef`。
全7repoのproof入力は不変。全言語gateは終了値1で、fallbackを訳文に数えない。

非公開世代の組立てSDKに続き、`pkgcore/runtime/pkg_generation_descriptor.*`と
`pkg_generation_publisher.*`へ論理世代公開を追加済み。設計はADR-0056、証跡は
`distribution/evidence/native-transition/publication-01/`。全stage予約を検査後も保持し、
全Managed guardと既存CAS/WALでroot/catalogのdescriptorを一つに確定する。
`generation.next`は未確定の作業ファイルで、起動器・読取器の権威ではない。
現行世代はroot.stateのaccepted planとCAS descriptorから読み、Active要求があれば
Indeterminateとなる。SDKのUID 0拒否を解除して稼働OSへ転用しない。
独立pkgcoreビルドと14 Ada main、stageの1,180・公開の333 assertions、root拒否7入口、
ソース24工程が成功。二つの新規ビルドで4アプリと14試験の18バイナリが一致した。
343入力hash、source subject、全7repoの不変proof入力を証跡へ保存している。
新runtimeはSPARK証明の対象外。本番認可、全DEB意味、catalog/holds、実mount/boot切替、
容量・同期故障・実電源断、rescue、新ISOは未完として続ける。

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
