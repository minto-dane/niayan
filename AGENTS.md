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

2026-09-10の最新指示: 着手済みの共有参照改善の比較・回帰確認を終えたら、本番デプロイを
妨げる未実装部分に集中する。追加の性能研究、試験器の拡張、同じ入力の再検証だけを主作業にしない。
試験は変更境界とリリース判定に必要な範囲へ絞り、検証済みで入力不変の工程は繰り返さない。
以下の一般的な検査手順より、この利用者の最新方針を優先する。
優先対象は実DEBの所有権・全効果とroot組立て、本番認可/供給provider、管理コマンドと実サービスの
接続、起動切替と復旧、完全置換ISOである。全言語翻訳等の既存製品要件も取り消されていない。
SDKと人工fixtureの成功を製品接続完了にしない。

2026-09-10 UTC。利用者指定により現在の自作コード・説明をBSD-3-Clauseへ統一した。
9 repositoryのLICENSEと895個の正本fileのSPDXを変更し、copyrightと過去のMIT許諾を保持した。
第三者原本・history・過去証跡は変更しない。共有vendor/profile/公開試験fixtureは正規工具で再生成し、
工具にlicense noticeの同期を追加した。make license-checkで現在の表記と正本/vendorの一致を確認する。

差分の分類では実行コードの860 fileがSPDX以外同一、三つが生成hash、三つが検査/同期工具の変更だった。
新しいlicense checkerと説明は別に追加した。意図しないアルゴリズム変更や保護履歴の変更はない。
root準備の予約FD、peer、権限制限と永続結果/公開/bootの分離も静的に見直した。
この範囲の確認をrepo全体の欠陥不在や独立監査と呼ばない。

固定SDKの新規exportで標準124工程、全75 Ada main、Python597発見/11skipが成功した。
標準subjectはe8835db7da6440f4ce5a86cc72cc00215860c727fac76fb5bbaabd3c576e9c8a。
その後の製品source差分はpackage copyrightの既存権利者一行だけで、全compile/testコードは同一。
最終subjectは4267f3a6f8668bcfb1283c270fbeaa04b9e97d81bb2095b67bdc9aec32ed4643。
初回二回は私有exportで参照文書を省略したためsource検査で停止。原本を補い、検査を緩めずに再開した。

BSDの最終主DEBとdbgsymは別directoryから再現した。主DEBのSHA-256は
538dda41e2357d74d9706626f9dc6ec721e82846fd54ec348a542bf8a62f54b9。
VMの実unit経由207 assertion、再起動後の履歴、三つのlock/設定欠損拒否と元inode復元が成功。
外側3 GiB/swap0/CPU1/pids128、VM2 GiB/1 vCPUで逐次実行し、全jobは終了済み。
旧証明を新subjectの成功へ読み替えず、全証明・旧カオス・性能campaignは再実行していない。
証跡はdistribution/evidence/licensing/bsd-01/、私有labはbsd-license-transition-01、判断はADR-0088。

必要時にghでminto-dane名義のrepository作成とReleases利用を行うことは利用者が許可済み。
ghの同名認証を確認した。改めて同じ許可を求めない。現時点ではremote作成・push・release公開は未実施。
公開予定はminto-dane/niaosと同ownerの8子repo。公開前に履歴・成果物・対応source・署名/連絡先を確認し、
既存repo/assetを上書きせず、未完成の成果物をstableと表示しない。詳細はdev/PUBLISHING.ja.md。

次は製品installer/controllerによるnative CAS初期化と独立認可/供給providerの実接続である。
全DEB効果、容量/物理再検証/回収、起動切替、完全置換ISOと全言語翻訳も引き続き未完。

以下は完了済みの前工程である。

2026-09-10 UTC。内部root準備の配布パッケージを追加した。
Debian標準のdebhelper/sysusers/systemdで専用nia-pkg account、root設定、保護mount、socket/serviceを
管理する。account名から実UIDを解決し、通常起動やpackage導入でbank/CASを初期化しない。
限定capability、読取専用device viewと一時領域、unit全体の資源上限と停止を実装した。

Debian 13 builderの別directoryで主DEBとdbgsym DEBが一致した。配布18入力も現行repoと完全一致。
最終レシピは対象をamd64へ限定し、vm-repackage-01で両DEBを再現してVM受入済みのbytesと同一と確認した。
主DEBのSHA-256は6013c429320602e42c657dcee90345bd21af81636af38f07b83e13f92c7ec75c。
vm-service-03で導入した実unitと専用UID 987から元人工DEBを展開し、207 assertionが成功した。
/devの四つのdevice、空の読取専用tmp、bankの保護mount、資源設定と二重初期化拒否を確認した。
同じ電源断済みdiskからの新規差分vm-resume-04では、後半だけを再実行して、再起動後の履歴、
bank lock/CAS lock/設定の欠損拒否、元inodeの明示復元後の履歴を確認した。

初回sysusers helper不足、/dev tmpfsとAPI mountの優先順位、欠損試験間のsocket停止持越しを修正した。
socketのtrigger制限はreset-failedだけでは解除されないため、既定windowも経過させる。
初回失敗も保存し、検査やrate limitを無効化していない。Ada driver/libraryは不変の同じbinaryを使い、
無関係な全suite・証明・旧カオス・性能campaignを繰り返していない。

対象subjectはa07ca45f3cc978710477f81e60e59403c1062e7fbdc6c4a5cb3b1facb2c5ee9a。
仕様はdistribution/native/service-deployment.ja.md、ADR-0087。証跡は
 distribution/evidence/native-transition/service-deployment-01/。外側3 GiB/swap0/CPU1/pids128、
VM2 GiB/1 vCPUを維持し、全VM/jobは終了済み。私有labはnative-service-deployment-01。

次は製品installer/controllerでのnative CAS初期化と、独立認可/供給providerを実サービスへ接続する。
今回のfixture認可は本番providerではない。容量予約、物理再検証/回収、全DEB効果、実boot、
完全置換ISOと全言語翻訳は未完。配布物の導入成功を公開コマンドや稼働rootの完成としない。

以下は完了済みの前工程である。

2026-09-10 UTC。既存native世代から内部root準備サービスへの実接続を追加した。
Prepare_Rootは世代/rootを保持してCASを再予約し、全保持内容と専用認可phaseを送信前後に検査する。
元tarと実予約FDをSCM_RIGHTSで渡し、サービスUIDと期待worker hashを照合する。
展開後の認可拒否はIndeterminateであり、非公開rootの完成を公開/boot成功にしない。
共有MC_Storeの借用予約FD APIは正本で追加し、正規工具でvendor・依存profile・公開fixtureを更新した。

固定SDKで関連二つのAda mainとC境界をcompileし、新規checkoutから同じ二つのbinaryを再現した。
同一binaryの旧世代処理1,211 assertion、実UID0拒否9場合を含む二つのmain、依存再生成17工程が成功。
VMのext4で元人工DEBからv5世代を作り、13 entryを実サービスへ展開した。通常と展開後認可拒否の
各207 assertionが成功し、保存intentと実native生成物も独立照合した。実行入力778個は全一致。
初回は境界fixtureの復元できないsymlink modeを正しく拒否した。元fixtureは保持し、別の
Linux復元可能なfixtureをgeneratorで作成。worker.jsonの有界診断を追加し、照合は緩めていない。

対象subjectはc4fe763e91ee4f77ed90a625feb04d34d2f42079da7aa850876d90fb8d26d489。
仕様はdistribution/native/root-preparation.ja.md、ADR-0086。証跡は
 distribution/evidence/native-transition/root-preparation-01/、最終VMはvm-prepare-03/。
外側3 GiB/swap0/CPU1/pids128、VM2 GiB/1 vCPUを維持。VM/jobは終了済み。
全suite・旧カオス・性能campaignを繰り返さず、新たな全コンポーネント形式証明とは報告しない。

次は本番service/account/mount/policy配置と独立認可/供給providerを接続する。
内部SDKの接続成功は公開管理コマンドの稼働受入ではない。容量予約、物理再検証/回収、
全DEB効果、実boot、完全置換ISOと全言語翻訳は未完。私有labはnative-root-preparation-01。

以下は完了済みの前工程である。

2026-09-10 UTC。非公開rootの永続準備bankを実装した。
内部coreのpeer UIDと実CAS予約inodeを確認し、SCM_RIGHTSの同じOFDをworkerまで保持する。
root所有の保護mountへintentをfsyncしてから展開し、結果を排他的に永続化する。
workerの予約FDの操作を制限し、親死亡時に停止する。SDKのUID0拒否と公開状態の正本は変更しない。

固定SDKで更新workerをcompileし、2 GiB/1 vCPUの使い捨てVMのext4で全7 inode kindと五つの
拒否場合、実peer/FD/worker、別予約・重複拒否、callerの予約維持、再起動後の履歴を確認した。
完全なintent bytesが見えた後にサービスをSIGKILLし、interruptedを確認した。worker実行中の
停止や物理電断とは認定しない。外側3 GiB/swap0/CPU1/pids128を維持。VMとjobは終了済み。

対象subjectはbbd17d3d2eca6f80f7a76970b324dc2c04800889e6205f884bb139f82a0479a5。
仕様はdistribution/native/root-bank.ja.md、ADR-0085。証跡は
 distribution/evidence/native-transition/root-bank-01/、最終実行はvm-bank-03/。
初回二回の試験側の未許可peer切断処理の失敗も保存した。変更境界の確認は完了し、
入力不変のAda suite・証明・旧カオス・性能campaignは繰り返していない。

次は同じ世代admission/保持検査と予約からbankへ渡す本番SDK adapterと製品service配備である。
準備権を世代認可と混同せず、inspectの履歴を物理再検証や公開/boot許可にしない。
容量予約、再検証/回収、全DEB効果、実boot、完全置換ISOと全言語翻訳は引き続き未完。
私有labはnative-root-bank-01、CONTINUE.jsonはこの工程の終了記録。

以下は完了済みの前工程である。

2026-09-10 UTC。非公開rootへ実ファイルを作成する内部workerを実装した。
認可側が渡す読取専用tar FDとprivate親FD、空root、nodev/nosuid/noexecを必須とする。
chrootと外側FD閉鎖、capability縮小、seccomp、512 MiB/有限期限を併用し、全入力hashと
復元可能なinode属性・内容を読み戻す。全属性cloneを保持せずstreamで再読する。
既存SDKのUID0拒否と世代wireは変更しない。結果は未公開のextractedまでである。

固定SDKで実compile、2 GiB/1 vCPUの使い捨てVMで全7 entry kind・10 entryを確認した。
ACL/xattr・数値所有者/権限・時刻・内容・hardlink・device番号、日本語とbinary名、
root時刻と五つの拒否場合、最終binaryの非特権拒否が成功した。外側3 GiB/swap0/CPU1/pids128を維持。
Distroboxのmknod拒否を全面的な制約解除で回避せず、read-only基準の新規VM差分で確認した。
最終subjectは864a37fa0fae58b6254ad8aa52167f221b0bf8023b34a1c0568eee98edb41e2d。
仕様はdistribution/native/root-extraction.ja.md、ADR-0084。証跡は
 distribution/evidence/native-transition/root-extraction-01/。最終実行はvm-stream/。

次は同じ世代認可/writer予約からworkerを起動する本番サービスと永続bankへ接続する。
今回のtmpfs展開は電断・永続媒体・抽出rootの起動受入ではない。ctime/birthtimeは原本履歴として保持し、
全Linux flags・全量容量まで認定しない。全DEB効果、controller復旧/回収、boot、完全置換ISO、
全言語翻訳も未完。入力不変のAda suite・証明・旧カオス・性能campaignは繰り返していない。
所有するVM/jobは終了済み。私有labはnative-root-extract-01、CONTINUE.jsonはこの工程の終了記録。

以下は完了済みの前工程である。

2026-09-10 UTC。元DEBの論理所有権をNIAGEN05の保持検査へ接続した。
共有directory、同名/versionのMulti-Arch:same共有inode、採用packageの直接Replacesを区別し、
失う全claimを確認する。仮想名・逆向き・推移的な上書き許可を使わない。
native architectureは同じcatalog/closureに束縛された保持intentから読む。
既存root/世代のwire形式を変えず、staging・公開・予約受渡し後・復旧・現在世代観測で必須にした。

固定imageと3 GiB/swap0/CPU1/pids128、JOBS=1で関連四つのAda mainをcompileした。
所有権279、root/実staging199、旧stage1211、旧公開2023、root公開/復旧142、UID0拒否7 assertion、
独立照合三つ、CI登録関連43検査が成功。登録75 main全体の再実行ではない。
対象subjectはff7439ce30fecc5c5c16794c59fced58948429d44e8d48914c67fc1effd34738。
仕様はdistribution/native/payload-ownership.ja.md、ADR-0083、証跡は
 distribution/evidence/native-transition/payload-ownership-01/。
768 pkgcore入力のbuildコピーとの差は再生成したCI登録だけで、全compile/test入力は一致した。
初回テストdriverの構文拒否も保存。上流DEBを変えず、自作root fixtureに必要なReplacesを明記した。

論理所有権はsite認可・全effectの実行ではない。conffile、diversions/alternatives、script/trigger、
旧世代からの実効果、特権分離した展開器、本番認可/供給provider、実サービス、起動切替/復旧、
typed GC、完全置換ISOと全言語翻訳は未完。次はこれら本番デプロイの未実装に集中する。
変更のない全体suite・証明・C sanitizer・native image・旧カオスcampaign・性能比較は繰り返していない。
私有labのjobは終了済み。

以下は完了済みの前工程である。

2026-09-10 UTC。NIAGEN05でNIAROOT1を世代manifest/pin・descriptor・既存公開計画へ接続した。
全pathの採用元を含むroot manifestとenclosing catalog/closureを照合し、一つの三entry batchで
catalog、tree、実tree/root.tarをstagingする。tar内属性を旧file-planへ切り詰めない。
公開・Engineへの予約受渡し後・記録済み復旧・現在世代のnative観測で保持検査を必須にした。
旧v1〜v4のbytesとtransaction導出を維持し、v4をroot成果物の認定としては使用しない。

固定imageの3 GiB/swap0/CPU1/pids128、JOBS=1で変更に関係する三つのAda mainをcompileした。
最終root組立て/実staging196 assertion、旧stage1211、旧publication2023、root公開/復旧142、
実UID0拒否4が成功。三つの独立照合とCI登録関連43回帰検査も成功した。
物理stagingの13 pathとaccepted stateから辿る10 pathについて、元DEBの全spanが一致した。
root manifestとtarの欠損を公開前に拒否した。root manifestはcommit拒否後の復旧と
accepted読取でも欠損を拒否し、明示復元後は供給期限を過ぎた記録済み公開を
既存の現在policy/Managed guardの下で復旧した。

最終subjectはeebfc077554d13fbc06738c47e2ca0711f9c428cb2c8c3b7a25dcc4bf491268a。
仕様はdistribution/native/root-generation.ja.md、ADR-0082。
証跡はdistribution/evidence/native-transition/root-generation-01/。
初回のstrict compile警告、最終v5検査順調整前の実行と最終実行を分離した。
変更のない全体suite・形式証明・C sanitizer・native image・旧カオスcampaignは繰り返していない。
74 Ada mainは登録数であり今回の実行数ではない。

この世代は実payload tarを保持するが、実OS rootへの展開・mount・bootではない。
所有権/効果の本番認可と独立供給provider、特権分離した展開器、全DEB効果、実サービス、
起動切替/復旧、全履歴typed GC、完全置換ISO、全言語翻訳を引き続き実装する必要がある。
同じ検証を反復せず、本番デプロイの未実装へ進む。現在の私有labのjobはすべて終了済み。

以下は完了済みの前工程である。

2026-09-10 UTC。本番root構築へ向けてPkg_Root_Archiveを実装した。全canonical pathの採用元を
明示し、選択した祖先directoryと同一原本hardlink targetを検査して、元DEBのlocal PAX/GNU
header・全属性・bodyを一つのtarへ保持する。NIAROOT1はcatalog/closure/payload/選択番号と
実tarを束縛する。旧file-plan、WAL、世代manifestの形式・認可条件は変更していない。

固定開発image、3 GiB/swap0/CPU1/pids128、JOBS=1で新経路をコンパイルした。
最終Ada131 assertion、実UID0拒否3 assertion、CI登録関連43回帰検査が成功した。
三つの人工元DEBから13 path・全7 entry kindを組み立て、独立したPython tarfile読取で
全選択spanと属性、hardlink targetの先行、manifestの全claim番号を照合した。
容量/期限、共有所有元、非directory祖先、別原本hardlink、manifest不整合、
実root tar/元DEB欠損と明示復元を確認した。初回の警告によるcompile失敗も保持した。

変更のない標準全体・形式証明・C sanitizer・native image・旧カオスcampaign・性能比較を
重複実行していない。74 Ada mainは登録数であり、今回全74本を実行した意味ではない。
仕様はdistribution/native/root-archive.ja.md、ADR-0081。
証跡はdistribution/evidence/native-transition/root-archive-01/。

新SDKは非特権candidate組立てまでである。Replaces/共有所有/conffileを含む本番所有権・
効果認可、世代pin/GCへの束縛、特権分離した実root展開、サービス接続とboot/復旧が次の実装対象。
8 GiBの出力上限に全量OSが収まるとは未認定。完全置換ISO・全言語翻訳も引き続き未完。
検証を主作業に戻さず、本番デプロイを阻む実装を進める。

以下は完了済みの前工程である。

2026-09-10 UTC。共有原本の前段検査を呼出し内の有界集合へまとめた。全固有原本の検査前には
native再構築を開始しない。個別の署名・policy・期限・元DEB/control照合とcatalog再観測は維持する。
API、永続形式、writer予約を変えず、検査結果のcacheを持ち越さない。

64個の小さい人工DEBと4×2 MiBの共有原本では、map作成21078→14740 ms、再検証21105→14821 ms、
保持検査3074→72 msだった。各条件一回の測定であり、本番全量性能の認定ではない。
全1/16/64 package条件でmap/catalog/closureが一致し、実read bytesでも重複削減を確認した。

統合確認の初回はディスク容量不足で84工程中8失敗となった。過去の成功を改変せず、
初回成功76工程のsource/logを照合し、失敗・未実行44工程だけを再開して120工程を満たした。
73 Ada main、map1088/publication2023 assertion、実TUF/OpenPGP→map40 assertion、実UID0拒否を確認した。
31 pkgcore実行物と18アプリの独立build一致、31 ELF検査も成功した。七つの数学的入力とC入力は不変で、
証明とC sanitizerを再実行していない。変更のないnative Python/image・私有D-Bus・host重複検査と
134件campaignも繰り返していない。今回は共有参照の実欠損・明示復元5場合を追加した。
使用中でない旧ISO01/03のhashを確認して削除し、約7.4 GBを回復した。受入済みISOと全対応ソース、
過去のbuild/受入記録は保持した。対象とhashはcapacity-recovery.jsonに記録した。

最終subjectは3da6f36e9b51de7ca3b0e35d5658d8e990826dad341917fb123b78c7dd2f043c。
証跡はdistribution/evidence/native-transition/shared-preflight-01/。重工程の3 GiB/swap0/CPU1/pids128、JOBS=1を維持した。
この性能改善はここで区切る。次は実DEBの所有権・効果・root組立て、本番認可/供給providerと
管理コマンド→実サービスの接続を進める。起動切替・復旧・完全置換ISO・全翻訳も引き続き未完である。

以下は前工程の供給ポリシーと実公開・復旧の記録である。

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
