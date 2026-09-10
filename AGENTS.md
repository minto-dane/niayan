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

2026-09-10 UTC。供給差集合と独立ポリシーを実公開計画へ束縛するNIASPOL1/NIAGEN04を実装した。
実root.stateとWALから新規admissionと記録済み復旧を区別し、復旧でも現在の独立key/floor/ageを必須にする。
Stage→Engineの予約受渡し後、実root/CAS予約の下で全状態・原本・intent・供給記録を再検査する。
公開後の遅いI/OはSTALEを返す場合があり、非OKを未実行と解釈しない。仕様は
distribution/native/publication-supply.ja.md、ADR-0080。旧形式のbytes/読取は維持し、公開はv4を必須とした。

最終subjectはa260ae0b1dbe60ba7d88e9057b7edbb2bece78a74a9cc4a9162226d1b62f2a54。
標準120工程・73 Ada main、map/policy 1029・stage 1211・publication 2023 assertionが成功した。
実TUF/OpenPGP→map接続40 assertion、native 359試験、host source24工程、標準/host各597 Python発見・11skip、
私有D-Bus32+10も成功した。31 pkgcore実行ファイルと18アプリの独立build一致、31 ELF検査、
C境界ASan/UBSanを確認した。七つの数学的入力集合は不変で証明を重複実行していない。
3374入力を新規・独立コピーと照合し、全11上位検査が成功した。

実公開・復旧経路で2 seed・134件の破壊的カオス試験と別検査器による照合を完了した。
EIO/ENOSPC40、SIGKILL40、必須参照欠損16、構造欠損14、反転/切断12、期限超過8、kill後欠損4。
故障直後・復旧後のroot.state/WAL bytes、実注入trace、署名と全原本を保持し、観測範囲で誤成功0。
復旧＋同じ計画の再実行＋読取検査は小fixtureで中央値2659/p95 2771/最大3137 ms。
欠損・破損の明示的lab復元を自動修復と数えない。最初の未完了69件と計測器・oracleの失敗も保存し、
修正後の134件とは分離した。製品dump禁止、3 GiB/swap0/CPU1/pids128、JOBS=1を維持した。
証跡はdistribution/evidence/native-transition/publication-supply-01/。

次は共有原本の反復hash・再観測の大規模性能を測定し、同じ予約内で共有検査できる範囲を実装する。
今回のpublisherは実root.state/WALを使うが、stage効果と独立observerは人工fixtureである。
本番供給/Managed provider、鍵/policy・独立時刻/floor、全DEB効果、実root/boot、typed GC、
完全置換ISO、全言語翻訳は未完。実TUF→mapの試験と本番publisher接続を混同しない。

以下は前工程の差集合mapと保存経路の記録である。

2026-09-10 UTC。新規に必要な元DEBの差集合と署名供給記録を完全一致させるNIASMAP1を実装した。
root identity・基準descriptor/closure・候補catalog/closureを結び、独立authorityと期限、全原本を検査する。
不変packageには新しいmirror掲載を要求しない。履歴保持の構造検査を新規認可として使わない。
仕様はdistribution/native/supply-map.ja.md、ADR-0079。実manifest/accepted planへの接続は未完。

最高添字の正規配列を誤拒否するoverflowを再現し、消費件数で位置を扱うよう修正した。
修正後の固定検証は標準120工程・73 Ada main・18アプリ、map 730 assertion、実署名接続40 assertion成功。
native 359試験、host source 24工程、標準/hostの各597 Python発見・11skip、私有D-Bus32+10も確認した。
31 pkgcore実行ファイルと18アプリが独立buildで一致し、31 ELF検査、C境界ASan/UBSanを通過した。
七つの数学的入力集合は不変で証明を重複実行していない。最終subjectは
6c6fb59c99442dd2973c420403ee37a3dd9e1ac7a10fcecdeda340a1444a8b2d。

新しいmap保存経路で二つのseedによる70件の破壊的カオス試験を完了した。
EIO/ENOSPC 13、SIGKILL 13、map破損6、必須参照欠損18、構造欠損8、期限超過8、kill後破損4。
実注入・失敗出力・同じmapへの再開を確認し、観測範囲で誤成功0。小fixtureの復旧中央値950/p95 1040/最大1121 ms。
復元は明示的lab操作であり自動修復ではない。未参照incomingの回収と物理電断・実root/bootの受入は未完。
製品dump禁止と3 GiB/swap0/CPU1/pids128制限を維持した。前の184件は別経路・別subjectの記録である。
最終・修正前・回帰失敗と注入traceはdistribution/evidence/native-transition/supply-map-01/に保持した。

次は実際に受理された基準とmapをmanifest/認可対象計画・保持rootへ同じwriter予約で束縛する。
新規admissionと記録済みtransactionの復旧を区別し、古い供給記録だけで新規実行を許さない。
共有索引の反復hash等の大規模性能は未認定で、実測と共有検査の設計が必要である。
製品key/policy/独立時刻floor、全DEB効果、実root/boot、完全置換ISO、全言語翻訳も未完。

以下は前工程の単一原本供給記録である。

2026-09-10 UTC。認証した原本をnative CASへ結ぶ、scope付き供給記録NIASUP01を実装した。
発行器は実TUF/OpenPGP認証と独立署名provider/keyを必須とし、nativeは記録の署名と期限、
必須6原本のCAS bytes、元DEBから再観測したcontrolを照合する。失敗時Bindingはzero。
仕様はdistribution/native/archive-receipt.ja.md、ADR-0078。全計画の網羅性と実行認可はまだ別である。
新規固定開発image 4ec0d3adaef0…で118標準工程・72 Ada main・18アプリを通過。
native imageは359試験、host sourceは24工程成功。標準とhostは各597 Python発見・11skip。
30 pkgcore実行ファイルと18アプリが独立buildで同一。C境界のASan/UBSan、実署名接続、実UID0拒否も成功。
七つの数学的入力集合は不変で形式証明を重複実行していない。対象subjectは
5727fd06deab52a4accf7bca5f48d61192df4936271b7e1a659ada887511bc27。
証跡はdistribution/evidence/native-transition/archive-receipt-01/。

最新依頼に従い、標準試験に加えて破壊的カオス試験を実施した。使い捨てCASに二つのseedで
184場合のEIO/ENOSPC、SIGKILL、kill後破損、全必須原本の破損/欠損、read遅延、
SIGSTOP/ロック競合/再開、構造欠損を注入し、実到達と拒否・再開を確認した。
観測範囲で誤成功0。回復は小fixtureで中央値171/p95 214/最大446 ms。明示的lab隔離・復元を
自動修復扱いしない。異常終了後の未参照incomingは残り得るため、有界な回収が必要。
dump禁止を変更せず、隔離labの計測権限だけを追加した。未成立の初期3試行も保持。
今後も重要な永続化経路には標準試験と有界な破壊的試験を併用する。物理電断・WAL全経路・
実root/bootは未認定。ホストの共有データ・実ディスク・時計に破壊を加えない。

次は公開計画が新規に必要とする全原本の供給記録を、保持閉包・検査記録・同じwriter予約へ束縛する。
既存の不変packageに新しいmirror掲載を一律要求しない。製品observer/key/policy配備、
rollback耐性のある時刻/floor、全DEB効果、実root/boot、完全置換ISO、全翻訳も未完。
開発image再構築ではOOMとmirror障害を検出・保持し、同じ依存を逐次導入する固定recipeで成功した。
制限は3 GiB/swap0/CPU1/pids128のまま。最終exportを含むピーク3 GiBを低い途中値で報告しない。

以下は前工程の保持TUF再検証と原本供給の記録である。

原本供給の返却前に、保持TUF checkpointを新しい上流Updaterで現在時刻に再検証する処理を追加した。
使用したroleと全top-level roleの最短期限を観測へ適用し、checkpoint/identity/予約の変更、
期限到達、時計逆行を拒否する。追加取得・第二の永続cache・初期rootへの復帰はない。
固定native imageで工具173/native153/hardening4/image16の計346試験が成功した。
新しい再検証16試験と原本接続15試験を含む。host・固定開発containerのsource検査は各24工程成功、
597試験発見・11skip。両実行の前後subjectは
fc04dac35a5edcfeee2e9da0b654dece78c257557df5ef5b526a841c4f72a1c8で一致した。
仕様はarchive-supply.ja.mdとrepository.ja.md、証跡はdistribution/evidence/native-transition/supply-revalidation-01/。
Ada・数学的入力には変更がなくbuild/proofは重複実行していない。以下は前工程の原本供給受入記録である。

Debian 13原本供給を共通TUF policyへ接続した。旧Forky固定の読取器をv2 policyで拡張し、
正確なcodename/pocket、suite、architecture、component、InRelease pin、日付floor、期限を検査する。
Trixie本体のValid-Until欠如にも独立の有限期限を要求し、期限付きmetadataは延命しない。
securityのcomponent宣言とindex pathを正しく対応付け、未使用Contentsのサイズを実読取と混同しない。
選択index、DEB、展開の容量上限は維持する。仕様はdistribution/native/archive-supply.ja.md、ADR-0077。

archive_intake.pyは既存TUF Repositoryで認証したv2 policyから、Debian署名、Packages、元DEB/controlを
照合し、native選択と比較する原本hashを返す。新規public CLI、第二DB、writer、署名鍵は追加していない。
旧v1は比較工具用に残すが共通native入口では拒否する。観測JSONを実行許可として使わない。
TUF再読取は同じ有界session内であり、最新remote policyのrefreshや実行時の認可ではない。

固定native test imageのmake image-checkで、工具173、native134、hardening4、image16試験が成功した。
新しい実OpenPGP試験15件と実TUF接続試験12件を含む。公開download CLIの実root検査6項目と
archive intakeの実UID0拒否も成功。ホスト・固定開発コンテナのsource検査は各24工程成功した。
Python単体試験597件発見、各source実行11件skipであり、skipを成功した実行に数えない。
両source reportの前後subjectは
aac58be4b71cb2356b1db2d5e55d371125483df1797d360882b4cd82076c3e5bで一致した。
3355入力を元repoと新規コピーで照合。七コンポーネントのdocs/engineering以外の入力と七つの
数学的入力集合は前工程c015455と不変であり、Ada build・71 main・再現性・証明を重複実行していない。
これらの既存runtimeの受入結果はpublication-intent-01に保持し、今回の新しい実行とは数えない。

公式Trixie本体・updates・securityのInRelease、b43-fwcutter元DEBと対応Sourcesの全3ファイルを
事前導入済みDebian keyringと明示したfingerprintで照合した。原本と公開鍵、対応ソースを保存し、
固定native image/networkなしで当初の観測時刻を指定して全結果を完全再現した。
公式原本のpinは検査時のローカル選択であり、本番Nia policy配備の認定ではない。実行・導入はしていない。
初回最小imageの全工具検査ではzstd不足を検出した。検査依存を追加し、tool-checkを標準native-checkへ
組み込んでからimageを再構築し、新規workspaceで最終検査した。初回失敗とその入力は保持する。
証跡はdistribution/evidence/native-transition/archive-supply-01/。

次は認証したpolicy/原本hashをnative CAS・保持閉包・検査記録・公開計画へ同じwriter予約で束縛する。
本番の鍵/policy配備、rollbackに耐える独立trust floor/時刻、全DEB phase・所有権・効果の認可も必要。
現世代fixtureのtree/versionはcatalog bytesであり、物理DEB payloadの適用ではない。
実root/boot、保護移行/初期構築、全履歴の保持とGC、完全置換ISO、全言語翻訳は未完である。

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
