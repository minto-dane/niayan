# Nia OS 開発・配布検証状況

2026-09-10 UTC。Debian 13ベースの起動・導入可能なKDE開発版。実ISOのVM受入を完了し、既存コンポーネントの実コンパイル、実行試験、再現性、独立Git管理も整備した。本番認定・実機認定は行っていない。

## 最新依頼: Niaへの完全置換とハードニング

### 直近の検証

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

### 前工程: 内部root準備サービスの配布

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

### 前工程: native世代からroot準備への接続

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

### 前工程: rootの永続準備bank

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

### 前工程: 非公開root展開worker

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

### 前工程: root世代の論理所有権

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

### 前工程: rootアーカイブの世代保持・公開・復旧

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

### 前工程: 元DEBからのrootアーカイブ組立て

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

### 前工程: 共有原本の前段検査

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

### 前工程: 供給ポリシーと公開・復旧

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

### 前工程: 原本差集合mapと保存経路

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

### 前工程: 単一原本の署名付き供給記録

認証した原本をnative CASへ結ぶscope付き署名記録NIASUP01を実装した。発行器が実TUF/OpenPGPを
検証し、nativeは独立key/scope/epoch floor/期限と全必須CAS原本を照合して元DEBのcontrolを再観測する。
完全成功時だけ記録のhashを返す。仕様はdistribution/native/archive-receipt.ja.md、ADR-0078。

新規固定開発imageで標準118工程・72 Ada main・18アプリ、私有D-Bus32+10試験が成功した。
固定native imageは工具173/native166/hardening4/image16の計359試験、skipなし。
host source検査24工程も成功。標準内とhostは各597 Python試験発見・11skip。
30 pkgcore実行ファイルと18アプリが別パス・mtime・TZ等で同一となり、C境界のASan/UBSan、
実署名接続5場合と実UID0拒否も成功した。七つの数学的入力集合は不変で証明を重複実行していない。
対象subjectは5727fd06deab52a4accf7bca5f48d61192df4936271b7e1a659ada887511bc27。

標準試験とは別に、二つのseedで計184場合の破壊的カオス試験を実行した。実CASのwrite/fsync/renameに
ENOSPC/EIOとSIGKILLを注入し、kill後の追加破損、必須原本の反転・切断・欠損、read遅延、
SIGSTOP中のロック競合と再開、構造欠損も検査した。注入の実到達、ACK、障害後のhashと再開を記録し、
誤った成功報告は観測していない。小fixtureでの再取り込み＋再検証は中央値171/p95 214/最大446 ms。
明示的なlab隔離・構造復元を製品の自動修復と数えない。異常終了後の未参照incomingは残り得るため、
有界な回収は今後必要。物理電断、WAL全経路、実起動切替のカオス受入は未完である。

証跡はdistribution/evidence/native-transition/archive-receipt-01/。初期のコンパイル・古いimageの依存欠落・
image buildのOOM/503・計測未成立も保持した。製品dump禁止とPCの3 GiB/swap0/CPU1/pids128制限は維持した。
次は全公開計画に必要な原本の供給記録と保持閉包・writer予約の束縛。本番鍵/policy配備、
全DEB効果、実root/boot、完全置換ISO、全言語翻訳も引き続き未完である。

### 前工程: 保持TUF metadataの返却前再検証

原本供給の返却直前に、保持TUF metadataを新しい上流Updaterで現在時刻に再検証する経路を追加した。
使用した委譲roleと全top-level roleの最短期限を観測期限へ反映し、checkpoint/identity/予約の変更、
期限到達、時計逆行を拒否する。現在のrootと唯一のtrust cacheを使用し、追加ネットワーク取得はない。

固定native imageの工具173/native153/hardening4/image16、計346試験が成功した。新しい再検証16試験と
原本接続15試験を含む。hostと固定開発containerのsource検査は各24工程成功、597試験発見・11skip。
両source実行の前後subjectはfc04dac35a5edcfeee2e9da0b654dece78c257557df5ef5b526a841c4f72a1c8で一致した。
原本と新規workspaceの入力を照合した。Adaと数学的入力は変更せず、build/proofの重複実行はない。
証跡はdistribution/evidence/native-transition/supply-revalidation-01/。供給認証とnative CAS・公開計画の
実行時の束縛、全DEB効果、実root/boot、完全置換ISO、全言語翻訳は引き続き未完である。

### 前工程: Debian 13原本供給の認証

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

### 前工程: 公開計画へ束縛するnative検査記録
公開計画へnative検査記録を束縛し、Publisherで必須の再検査を行う経路を実装した。
NIAGEN03はNIAGINT1のCAS hashを含み、正確な基準descriptor、候補catalog/保持閉包、
architecture policy、最終集合又は通常更新の結果を既存の認可対象計画へ結び付ける。
実root.stateから基準を照合し、元DEBから結果を再計算する。既存Managed guardも必須である。
CAS予約は実行器への既存の受け渡しで解放するため、公開全区間で連続するとは主張しない。
仕様はdistribution/native/publication-intent.ja.md、判断はADR-0076。

新規workspaceの標準make check private-dbus JOBS=1で全116工程、18アプリ、71 Ada mainが成功。
私有D-Bus32+10試験、ホストsource検査24工程も成功した。Python単体試験582件発見、
source実行11件skipであり、skipを成功した実行に数えない。公開/復旧1638、stage1202 assertions。
全体検査とhost sourceの前後subjectは
5c4bcdd2d488b40e6cf4a2582ca5171121ff281528febda7ccfd2f971ec42b9aで一致した。

異なるmtime/作業パス/TZの新規独立buildと、29実行ファイル・全18アプリが一致した。ELF検査も成功。
workspace3350入力を3コピー、pkgcore731入力を4コピーで照合した。
単独CI25 main、root拒否8本、別の新規コピーのASan/UBSan stage/公開実行も今回の入力で成功した。
sanitizerはC境界等の検査で、Ada・上流library本体は非計測、leak検査は無効。
全7repoの数学的入力、guardとscope工具は不変。形式証明の重複実行はなく、世代runtimeはSPARK対象外。

独立readerは二つの公開済み検査記録と結果を元DEBから照合した。保持欠落73、不正記録26ケースと、
組立て完了済みの不正候補3種類の公開拒否を確認した。後者ではroot.stateとgeneration.nextの内容を維持する。
二世代の16 catalog観測、18更新観測、四Binding、候補保持8欠落も維持した。
保存snapshotはsanitizer実行の最終状態で、独立readerの結果は通常CIと完全一致する。
新しいPublishはNIAGEN03だけを認め、旧版計画の再実行も拒否する。旧版の途中transactionは
保持した旧実装で復旧を終えてから移行する必要がある。旧版の本番移行は未認定。
証跡はdistribution/evidence/native-transition/publication-intent-01/。
三回の診断失敗と追加試験前の第四診断成功も、当時の入力とともに保持した。

次は本番供給認証/policy adapterを、正確な検査記録と同じ認可対象計画へ接続する。
検査記録の存在だけで供給・同意・全DEB phase・所有権・効果の認可を置き換えない。
現fixtureのtree/versionはcatalog bytesであり、物理DEB payloadの適用ではない。
版付き世代属性、実root/boot、保護移行/初期構築、全履歴の保持とGC、完全置換ISO、全言語翻訳は未完である。

### 前工程: 更新計画の全体検査完了
更新計画の標準全体検査を完了した。前工程では小さい人工プロセスに実証明用の合計RSS枠2048 MiBが
適用され、利用可能メモリ4096 MiBを要求していた。人工試験の合計枠も128 MiBへ厳しく限定した。
ホスト予備2048 MiB、実証明の既定枠2048 MiB/開始4096 MiB、guard実装と外側cgroupは変更しない。
人工試験にも実際の予備メモリと全実行枠を要求し、起動可能と偽装していない。
追加した二つの境界試験は、人工枠と既定の実証明枠それぞれについて、余裕不足なら子を起動しないことを検査する。
guard試験17件、開発基盤134件が成功した。詳細はADR-0054、REQ-095、FAULT-092。

新規workspaceの標準make check private-dbus JOBS=1で全116工程、18アプリ、71 Ada mainが成功。
私有D-Bus32+10試験、ホストsource検査24工程も成功した。Python単体試験582件発見、
source実行11件skipであり、skipを成功した実行に数えない。公開/復旧1361、stage1193 assertions。
全体検査とhost sourceの前後subjectは
f6e883af2ab0a8b15ffaeb61f2cf2d8718b7513def47b3143fd131514e63d8abで一致した。

異なるmtime/作業パス/TZの新規独立buildと、29実行ファイル・全18アプリが一致した。ELF検査も成功。
workspace3346入力を3コピー、pkgcore729入力を4コピーで照合した。
最初の全体runnerはTZ/SOURCE_DATE_EPOCHを子へ渡さず、独立buildには変更TZと固定epochを渡す。
pkgcoreの全入力と29実行ファイルは前工程とも完全一致する。そのため単独CI25 main・独立oracle、
root拒否8本、ASan/UBSanの既存証跡は同じ入力と成果物へ対応付け、今回の再実行とは数えない。
今回の全体Ada実行は新たに記録した。sanitizerはC境界等の検査で、Ada・上流library本体は非計測、leak検査は無効。
全7repoの数学的入力、全guardとscope工具は不変。形式証明の重複実行はなく、世代runtimeはSPARK対象外。
証跡はdistribution/evidence/native-transition/current-transition-02/。
前工程current-transition-01の失敗と部分検証は当時のsourceに束縛したまま保持する。

Read_Current_Transitionは正確なdescriptor、候補catalog/保持閉包、architecture policyから
同じpublication/root/CAS予約で通常更新を検査し、NIAUPD01へ束縛する。
返却時に予約を解放するため本番admissionの許可ではない。仕様はdistribution/native/current-transition.ja.mdとADR-0075。
次は本番認証/policyとBindingを同じwriter予約へ結び、全DEB phase・所有権・効果と版付き世代属性を進める。
現在の公開の構造検査だけをnative適用認可にしない。保持中の同じlockを外部read APIで取り直す接続も避ける。
実root/boot、保護移行/初期構築、全履歴の保持とGC、完全置換ISO、全言語翻訳は未完である。

### 前工程: 確定済み世代からの更新計画と部分検証

確定済み世代に束縛した更新計画をRead_Current_Transitionへ実装した。
正確なdescriptor hash、候補catalog/保持閉包、architecture policyを指定し、同じpublication/root/CAS予約で
前後の原本・保持・通常更新を検査する。NIAUPD01へdescriptor、候補、保持、transition fingerprintを束縛する。
失敗はdescriptor/plan/bindingの旧成功も消す。予約は返却時に解放し、本番admissionの許可とは扱わない。
仕様はdistribution/native/current-transition.ja.md、判断はADR-0075。

今回の全体検査は未成功。標準make check private-dbusはengineering単体試験で安全ガードが
insufficient-memory-before-startを返し、全体のAda実行前に停止した。開始条件はsession 2 GiB + reserve 2 GiB。
上限・reserve・guardを変えず、利用者のアプリを停止していない。再実行には実際のメモリ余裕が必要。
ホストsource検査も未完。前工程の全116工程/71 main成功を今回の入力へ流用しない。

別に新規コピーから全sourceの通常コンパイルと18アプリ、pkgcore25 mainを構築した。
独立側の単独pkgcore CIは全25 mainと独立oracle、898ケースの依存比較・44ケースの更新比較が成功。
公開/復旧1361 assertions、stage1193 assertions。18更新観測・四Binding・候補保持8欠落を
独立readerで照合した。基準保持欠落と既存復旧行列も維持する。root拒否8本の公開driverは40 assertions。
ASan/UBSanリンク下の公開1361 assertionsが成功。Adaと上流library本体は非計測、leak検査は無効。
29実行ファイルと全18アプリが独立buildで一致し、ELF検査も成功した。
pkgcore729入力を4コピー、workspace3346入力を3コピーで照合。私有D-Busは32+10試験成功。
最初の通常buildはTZ/SOURCE_DATE_EPOCHを明示的に外し、独立buildは変更mtime/TZと固定epochを使った。
数学的入力は全7repoで不変。変更runtimeはSPARK対象外であり、新しい形式証明とは数えない。
source subjectはafdb6163195025cb2c485c7450ee4894738ba2f51b6a767930753921023e2cb8。
部分検証の証跡はdistribution/evidence/native-transition/current-transition-01/。
再起動後の旧Podman runroot拒否とメモリ不足の全体検査も保存した。
引き継ぎ文書だけの後続変更は別に記録し、ビルド時入力一覧を書き換えない。

次はメモリ余裕を確保後、同じsourceの全体source/build/71 main検査とホストsource検査を完了する。
scratchは/home/nia/devbox/niaos/.work/native-generation-transition-01/、固定container helperはrun-container.py。
workspaceとworkspace-independent-long-pathのソースは変更していない。code変更時は新規build treeを作る。
全体検査の失敗記録を上書きせず、再実行ログと成功したreportを別に保存する。証明入力不変なら再証明しない。
その後、本番認証/policyと同一実行予約へのBinding接続、全phase・所有権・効果・世代属性を進める。
全履歴の保持とGC、保護移行/初期構築、実root/boot、完全置換ISO、全言語翻訳は未完である。

### 前工程: 世代manifestへのcatalog保持束縛

NIAGEN02へcatalog保持閉包のhashを束縛し、stage/publication/現世代native観測へ接続した。
旧NIAGEN01の予約byteとtransaction導出、構造検査を維持する。native公開とnative観測は新版を必須とし、
既存世代transaction pin → manifest → closure → 全掲載objectを検査する。第二の保持DBや重複pinは作らない。
全掲載objectの欠落検査をcatalog再構築より先に行い、再生成で欠落を隠さない。
Stageの四入口とPublishは有限BOOTTIME Deadlineを必須とし、認可callbackの前後にも検査する。
期限切れの部分状態は保持し、未実行と読み替えない。CAS予約は実行器への移行時に解放するため、
公開の全区間でCAS lockを保持しているとは主張しない。将来のGCは既存pinの参照と予約規則を守る必要がある。

固定環境の新規workspaceで全source・18アプリ・71 Ada main、全116工程が成功した。
私有D-Busは32+10試験成功。Python単体試験580件発見、source実行11件skipで、skipを成功実行に数えない。
世代stageは1193、公開/復旧は1133 assertions。二世代の保持一覧は5/7 objects、240/304 byte。
64通りの閉包自身/member欠落、五境界での状態不変と非再生成、期限・認可中の期限切れ、旧形式公開拒否を検査。
独立readerが実root.stateから原本まで照合し、故障試験の実行集合も比較した。16回のnative観測を照合した。
段階検証では期限検査後の不正hash拒否status回帰を既存試験が検出して修正した。
遅延認可試験はManaged内部の再認可8回を許す正しい期待値へ修正し、Staleと状態不変を維持した。
失敗した診断のsource入力一覧・該当source・ログも別に保持する。

同じ全体buildの単独pkgcore CIは全25 mainと独立oracle、上流との898ケース比較が成功。
pkgcore29実行ファイルと全18アプリは独立buildで一致し、ELF検査も成功。
pkgcore729入力を4コピー、workspace3344入力を3コピーで照合した。
全体runnerはSOURCE_DATE_EPOCH/TZを子へ渡さない。二回目は固定epoch・変更mtime/TZを渡し、環境差を証跡へ記録する。
root拒否8本とASan/UBSanリンク下stage1193・publication1133 assertionsも成功。
Ada・上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変、変更runtimeはSPARK対象外。
ソース24工程も成功し、全体検査と同じ前後subjectは
`139a883e127a3d94aa964d0f2fc2883346a7277f83c40c4a54dcc076e9ca1384`で一致した。
証跡はdistribution/evidence/native-transition/generation-retention-01/、判断はADR-0074、仕様はdistribution/native/generation-retention.ja.md。

全OS/最大容量、全履歴・効果・認証・復旧rootの保持と安全なGC、本番の認証済み予約、保護移行/初期構築、
実行phase・所有権/alias・全効果、実root/boot・完全置換ISO・全言語翻訳は未完。
次はcatalog選択・transition・保持hashを本番admissionと同一予約へ結び、実行phaseと全属性の世代組立てを進める。
旧file planへnative属性を切り捨てず、任意scriptをhost rootで実行しない。テスト用authorityとtree/versionを製品の実行器と混同しない。

### 前工程: catalog由来のCAS保持閉包

Native catalog由来のCAS保持閉包を実装した。Pkg_Catalog_Retentionが全原本・control内容・
圧縮/展開data・payload内容とlink文字列・xattr/ACLの正確な集合を再観測し、NIACLOS1へ保存する。
Prepareは明示的なcache再構築、Verifyは全掲載objectの存在/hashを先に検査してから正確な集合を比較する。
省略・余剰を認めず、欠落を再生成で隠さない。Pin/Verify_Pinは既存immutable CAS pinを使い、別用途のidentityを上書きしない。
全APIのUID0拒否・期限・失敗出力zeroを維持。object/pin削除・accepted state更新・script実行はない。
合成5原本の二catalog（21 objects/752 byte、15 objects/560 byte）を独立readerで原本から照合した。
保存driverは320→550 assertions。35不正一覧、21 memberの個別欠落、破損byte、pin再open/衝突、明示再構築を検査。
追加原本は圧縮control/data、script内容、七payload種、非空xattr/ACLを含む。rich catalogのpayload hashは
保存catalogとの束縛確認であり、この追加oracleによる全payload index再計算とは数えない。

全workspaceの新規build treeで全source・18アプリ・71 Ada main、全116工程が成功した。
私有D-Busは32+10試験が成功。Python単体試験は580件発見、source実行時11件skipで、skipを成功実行に数えない。
単独pkgcore CIの全25 mainと独立oracle、上流との898ケース比較も成功。既存の公開/復旧456 assertionsを維持した。
全体検査で世代公開driverの相対媒体path処理を修正した。FS SDKのabsolute-only条件を弱めず、driverのFull_Nameで正規化する。
最初の検証コピーで参照先の証跡文書6件が欠けていた記録と、媒体pathの失敗も別に保持した。
新規treeで全体検査をやり直し、同じ実行ファイルで単独CIの絶対path経路も確認した。

pkgcoreの29実行ファイルと全18アプリは、それぞれ独立buildで一致し、ELF検査も成功。
pkgcoreの729入力を4コピー、workspaceの3342入力を3コピーで照合した。
全体検査runnerはSOURCE_DATE_EPOCH/TZを子へ渡さない。二回目は固定epoch・変更mtime/TZを渡し、実際の環境差を証跡に記録する。
root拒否8本（catalog driver11 assertions）とASan/UBSanリンク下550 assertionsも成功した。
Ada・上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変、新規runtimeはSPARK対象外。
ソース24工程も成功し、全体検査と同じ前後subjectは
`b5d4d412c0d4f11d741f030cb08180d9d2e8534bf73883c8dad8323f2d38127c`で一致した。
証跡はdistribution/evidence/native-transition/catalog-retention-01/、判断はADR-0073、仕様はdistribution/native/catalog-retention.ja.md。

全OS/最大容量、世代・効果・認証・復旧rootを含む保持と安全なGC、本番の認証済み予約、保護移行/初期構築、
実行phase・所有権/alias・全効果、実root/boot・完全置換ISO・全言語翻訳は未完。
次は版付き世代manifestへ保持hashを束縛し、stage/publication/現世代native観測の同じ予約へ接続する。
旧NIAGEN01の予約領域を無断転用せず、既存pinを別の型で上書きしない。欠落検査より先にcatalog Loadを呼んで再生成しない。

### 前工程: 受理済みcatalogの同一予約での観測

受理済み世代のnative catalog観測をpublication/root/CASの同じ排他区間へ接続した。
Read_Currentと共通の内部処理でaccepted plan・descriptor・manifest pin・journalを検査し、
新しいRead_Current_Catalogが全元DEBからcatalog/payloadを再観測する。最後に状態と期限を再確認する。
失敗はdescriptor/catalog/payloadの旧成功も消す。記録だけのRead_Currentをnative検査済みとは数えない。
返却前に予約を解放するため、観測は長時間の更新許可ではない。Publishの正確なpredecessor比較とmanaged guardを維持する。
固定環境で全source・4アプリ・25 Ada main、公開/復旧試験456 assertions（従来333）が成功した。
二つの合成native catalogと16回の成功観測、既存の拒否/復旧、原本/catalog欠落、root/CAS競合、期限、別root、旧plan拒否を検査。
独立readerが実際のroot.state→accepted plan→descriptor lineage→manifest→catalog→元DEBの関係を通常CIで照合した。
29実行ファイルは独立二ビルドで一致し、725入力をcheckoutと全検証コピーへ照合した。
29 ELF、8本のroot拒否driver（公開driver37 assertions）、ASan/UBSanリンク下456 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変、変更runtimeはSPARK対象外。
ソース24工程は成功し、前後subjectは
`4694cfb40880ec35fcb93b8c30fb94d2dbcab4121f091745462ea2aed78a9be7`で一致した。
固定SOURCE_DATE_EPOCHで増分診断の実行ファイルが更新されない挙動を観測し、未採用の記録として保存した。
新規ソースコピーの全build treeでやり直した。dev/READMEの新規build tree必須条件に従う。
試験のauthorityとtree/versionは合成であり、DEB payloadの物理適用ではない。
全OS/最大容量、本番の認証済み予約、CAS pin閉包、保護移行/初期構築、実行phase・所有権/alias・全効果、
実root/boot・完全置換ISO・全言語翻訳は未完。次はcatalogと原本・生成物の保持閉包、実行phaseと本番admissionを進める。
詳細はADR-0072、distribution/native/current-catalog.ja.mdとcurrent-catalog-01証跡。

以下は直前のcatalog保存工程の記録。

正規catalogのCAS保存と元DEBからの再構築SDKを追加した。
既存NIACSEL1のpreimageをそのまま保存し、fingerprintと同じCASアドレスを使う。第二の導入済みDBは作らない。
読取時に正規長/版/件数/順序/全digestを検査し、全原本のcontrolとpayloadをnative readerで再観測する。
期待control、payload index、最終catalog hashが完全一致してから両出力を返し、失敗は旧成功も消す。
空payload原本が欠けてもcacheで代用しない。Save失敗は入力を保持し返却アドレスをzeroにする。
固定環境で全source・4アプリ・25 Ada main、新320 assertionsが成功した。
4合成原本の全identity・44関係項目/15atom・3claim、20形式不正、原本/catalog欠落、期限を検査した。
独立ar/tar readerがpayload index・全metadataと保存CASの実byte列を通常CIで照合した。
440 byteの正規catalogは`89a31cbefdb7297293dc8b7a7315adfadccc79dcaffc580e5ac254d9610ee44f`で、従来のfingerprintと一致。
既存の最終集合898ケースと固定dpkg simulation、更新44ケースも再度成功した。
29実行ファイルは独立二ビルドで一致し、724入力をcheckoutと全検証コピーへ照合した。
29 ELF、8本のroot拒否driver（新7 assertions）、ASan/UBSanリンク下320 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変、新runtimeはSPARK対象外。
ソース24工程は成功し、前後subjectは
`cc7c7d9b771e5a9b784d0a926f52eb04ee5924eb73c82997c8fbd7ed98f364af`で一致した。
全OS/最大容量、供給認証、accepted generationとの同一reservation下照合、CAS pin閉包、
保護移行/初期構築、実行phase・所有権/alias・全効果・実root/boot・完全置換ISO・全言語翻訳は未完。
次はこの永続原本を世代の観測・同一reservation下の照合へ結び、保持閉包と実行phaseの条件を進める。
Publisher.Read_Currentは返却前に内部lockを解放するため、観測を長時間の更新許可として流用しない。
詳細はADR-0071、distribution/native/catalog-store.ja.mdとcatalog-store-01証跡。

以下は直前の更新計画工程の記録。

既存世代からのnative変更集合と保護対象の検査を追加した。
前後catalogの正確なname/architectureと原本を照合し、追加・削除・更新・降格・再梱包を区別する。
target最終集合を内部で再検査し、旧Essential/Protectedの削除・architecture変更・flag消失を
通常更新で拒否する。異名Provides/Replacesでの代替は保持とみなさない。保護移行の許可は別途必要。
全体成功時だけ前後catalog/endpointと全deltaをhashへ束縛し、失敗では旧成功/部分計画を消す。
前世代の依存破壊を修復でき、入力順と寿命に依存しない。非空catalog契約は変更していない。
固定環境で全source・4アプリ・24 Ada main、新3045 assertionsが成功した。
36合成原本・44ケース（通常23、保護拒否17、target拒否4）は独立した原本/control・delta/hash計算と一致。
既存の最終集合898ケースと固定dpkg simulationも再度一致した。実phaseの受入ではない。
28実行ファイルは独立二ビルドで一致し、720入力をcheckoutと全検証コピーへ照合した。
28 ELF、7本のroot拒否driver（新transition5 assertions）、ASan/UBSanリンク下3045 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変、新runtimeはSPARK対象外。
ソース24工程は成功し、前後subjectは
`646d1c1d56d1adb351034dee09978af06516d47a531fdc11a0acfc2160888c65`で一致した。
全OS/最大容量、認証済みbaselineのguard下照合、検証済み保護移行、bootstrap、rollback floor、
実行phase・所有権/alias・全効果/CAS pin閉包・実root/boot・完全置換ISO・全言語翻訳は未完。
次は現在の稼働世代との束縛と、実行phase・過去の構成版・所有権の条件を進める。
接続調査では、generation manifestはcatalogのCAS原本を要求するが、selected catalogは
現状fingerprintだけを計算し、その正規byte列の保存/原本からの再構築APIがないことを確認した。
既存NIACSEL1のhashを変えずCASへ保存し、読取時に全原本/control/payloadを再観測する経路が先に必要。
第二の導入済みDBを作らない。Publisher.Read_Currentは内部lockを返却前に解放するため、
その観測だけを長時間の更新許可とみなさず、admissionの同一reservation下で再照合する。
詳細はADR-0070、distribution/native/transition-plan.ja.mdとtransition-plan-01証跡。

以下は直前の最終集合検査工程の記録。

sealed候補のnative最終集合検査を追加した。
全Depends/Pre-Depends group、実名と全Providesの版/architecture、Conflicts/Breaks、同名Multi-Arch共存と版を検査する。
成功時だけcandidate/architecture policy/rule versionのreceiptを返し、失敗時は旧成功hashを消す。
初期610ケースで同名別architectureの自己Breaksが上流と異なり、instance単位の例外へ修正した。
negative virtualのarchitecture指定も追加した898ケースは固定dpkg 1.22.22の個別configure/unpack simulationと一致。
参照はprivate模擬statusと空payload/no-script合成DEBのみ。製品backendや実phase順序の証明ではない。
固定環境でpkgcore全source・4アプリ・23 Ada main、新23038 assertionsが成功した。
153原本の898ケースは原本/control・source index・catalog・policy/receipt hashの独立計算とも一致。
fixture再生成・native matrix・独立hash・上流simulationを通常の生成CI runnerへ組み込んだ。
27実行ファイルが独立二ビルドで一致し、677入力をcheckout・通常・独立・sanitizedコピーへ照合した。
27 ELF、root拒否（新final-set5 assertions）、ASan/UBSanリンク下23038 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変、新runtimeはSPARK対象外。
ソース24工程は成功し、前後subjectは
`0af8311a792c22aff260302f937ca135efe9a7b04162a70e2427efa7d6e8a34d`で一致した。
全OS原本集合や最大capacityの受入は未実施。認証済みresolver/policyと同意への接続、実行phaseと既構成版、
Essential/Protected削除、source保持/weak依存policy、実効所有権とalias、全効果・CAS pin閉包、
稼働catalog/guard・実root/boot・完全置換ISO・全言語翻訳は未完。
次は既存世代・実行phase・実効所有権の条件と、認証済みresolver/管理器への接続を進める。
[実装境界](distribution/native/final-set.ja.md)、[検証記録](distribution/evidence/native-transition/final-set-01/README.ja.md)。

### 直前の選択catalog検証

選択原本・期待control・payload索引を完全照合するnative candidate catalogを追加した。
公開Observationを信用せずCAS原本を再観測し、全identityと11関係項目のatom/groupをcompactに保持する。
同一原本、同一name/architectureの二版・再梱包、空package欠落と同数の別原本混入を拒否する。
失敗は全candidateをClearし、再Sealでも入力を照合する。入力順とpayload寿命に依存しない。
固定環境でpkgcore全source・4アプリ・22 Ada main、新313・既存payload814/index449 assertionsが成功。
4合成原本44関係項目/15 atom、13元DEBと大型合成原本154項目/146 atomを独立control読取と照合した。
4原本のpayloadは今回独立tar/CAS照合済み。14原本のpayloadは新native scanで再観測し、前回の独立検査へ
原本集合とhashを完全照合した。後者のscanは87.464秒・最大RSS36,760KiBで、全OS/最大容量の受入ではない。
26実行ファイルが独立二ビルドで一致し、516入力をcheckout・通常・独立・sanitizedコピーへ照合した。
26 ELF、root拒否（新catalog8 assertions）、ASan/UBSanリンク下313 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変で、新runtimeはSPARK対象外。
ソース24工程は成功し、前後subjectは
`06761e213cb6194f7ce7f491719cd47fccfc72e6d3e213b2c0882caa329b198a`で一致した。
選択リストを認証済みresolver/policyへ結ぶguard、全関係の成立・Multi-Arch共存/phase、実効所有権とalias、
全効果・CAS pin閉包・稼働catalog/guard・実root/boot・完全置換ISO・全言語翻訳は未完。
次は、このprivate候補を使って最終集合のnative関係とphase/所有権の条件を実装する。
[実装境界](distribution/native/selected-catalog.ja.md)、[検証記録](distribution/evidence/native-transition/selected-catalog-01/README.ja.md)。

### 直前の原本claim索引検証

全原本の属性・所有権主張を保持するnative索引を追加した。
追加順に依存せず、原本digestとsource ordinalでhardlinkのinodeを区別する。
共有pathの全ownerと属性差、暗黙parent、非directory祖先を保持し、実効ownerは選択しない。
失敗時に候補全体をClearし、全体seal前の候補を公開しない。入力inventoryの破棄後も索引は変わらない。
固定環境でpkgcore全source・4アプリ・21 Ada main、新449・既存payload814 assertionsが成功。
14合成原本35 claim/28 path、13元DEBと大型合成原本の2904 claim/2493 pathを独立tar/CASとhash計算へ照合した。
両集合とも逆順で同じfingerprint。元DEB集合の索引process最大RSSは20,624KiBだった。
対象入力の測定であり、最大4096原本・524288 claim・256MiB名の実負荷受入ではない。
25実行ファイルが二ビルドで一致し、503入力をcheckout・通常・独立・sanitizedコピーへ照合した。
25 ELFの緩和設定、root拒否（新index6 assertions）、ASan/UBSanリンク下449 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。新runtimeはSPARK対象外で、全7repoのproof入力は不変。
最終ソース24工程は成功し、その実行前後subjectは
`d8d464830a283c50c37cfc7c907db77ed80c0a90d90c6f3bce7b20dddca1bd77`で一致した。
索引の原本集合と認可されたresolver集合の一致、package identity/版/architecture、Replaces/Multi-Archとalias、
実効所有権・全効果・CAS pin閉包・稼働catalog/guard・実root/boot・完全置換ISO・全言語翻訳は未完。
[実装境界](distribution/native/payload-index.ja.md)、[検証記録](distribution/evidence/native-transition/payload-index-01/README.ja.md)。

### 直前のimage候補検証

未改変の上流工具による世代image生成を調査した。
固定erofs-utils 1.8.6-1のtar直接入力は19回中17回でimageを生成し、
その17個のfsckと追加4組のbyte再現性は成功したが、独立読戻しでACL欠落・
PAX小数時刻の不一致を確認した。前方hardlinkとGNU負時刻は構築失敗した。
この経路を本番backendには採用せず、原本の属性要件を維持する。
失敗した疎ファイルの証跡コピーは停止して部分出力を削除し、最終保存を有界にした。
実験は合成入力のみで、runtime・共有contract・proof入力・ISOの変更はない。
ソース整合性24工程は成功し、前後subjectは
`8a6ce83352a1d8e86165e2af6428427b5b9e0b67909623ca66685aabd7c2e17d`で一致した。
[判断と次の条件](distribution/native/generation-image.ja.md)、
[実験証跡](distribution/evidence/native-transition/generation-image-01/README.ja.md)。

### 直前のpayload実装検証

元DEBのtar内容・属性・リンクを保持するnative SDKを追加した。
独立framingと上流readerを照合し、全体成功後にprivate inventoryを返す。
通常内容と属性blobは既存CASへ保持し、前方hardlink・全permission bit・UID/GID・
正確なPAX時刻・多言語名を扱う。Unicode正規化で別名を同一化しない。
固定環境で全ソース・4アプリ・20 Ada main、新payload814 assertionsが成功した。
C.UTF-8とCのcaller locale、40合成DEBの再生成、11合成入力28 entryの独立oracleが成功。
13元DEBと大型合成DEBの2,904 entry・計166,123,520 byteも独立tar/CAS照合に成功した。
大型100,669,440 byteのnative子process最大RSSは16,640 KiB。当該入力の測定である。
二ビルドの24実行ファイルが一致し、494入力をcheckout・各検証コピーへ照合した。
root拒否3 assertions、24 ELF、ASan/UBSanリンク下814 assertionsも成功した。
Adaと上流libraryのコードは非計測、leak検査は無効。新runtimeはSPARK対象外。
ソース24工程の前後subjectは`32956b52274683d893c1d0c5824d22e45b4ea8f25daa1af78370666a37fa90bc`で一致し、全7repoのproof入力は不変。
採用profile外のglobal PAX・sparse・ACL方言は拒否し、全対応済みとはしない。
既存世代v1にはhardlink・setuid/setgid/sticky・全時刻等を渡せないため、
versionを持つ世代形式・実行器と所有権管理の拡張が次の必要工程である。
全DEB効果・稼働catalog/認可・実root/boot・完全置換ISO・全言語翻訳は未完。
[実装境界](distribution/native/deb-payload.ja.md)、[検証記録](distribution/evidence/native-transition/deb-payload-01/README.ja.md)。

### これまでの検証（各時点の範囲）

元DEBのdataメンバーを64 KiBずつ展開し、原本・展開物を既存CASへ束縛するSDKを追加した。
無圧縮・gzip・bzip2・LZMA-alone・xz・zstdの単一完全streamを扱う。
二回の展開でhash・サイズを再照合し、全入力/出力を同時にメモリへ確保しない。
固定環境の全コンパイル・4アプリ・19 Ada main、新stream389・関係176・メタデータ117・制御229・envelope764 assertionsが成功。
43 fixtureファイル（30合成DEB）の再生成照合、13元DEBと大型合成DEBの独立ar/Debian読取工具/CAS照合も成功。
計166,123,520 byteを比較し、大型100,669,440 byteの展開時のnative最大RSSは14,660 KiBだった。
当該入力での測定であり、全形式のメモリ証明ではない。二ビルドの23実行ファイルが一致し、446入力を照合した。
C境界のASan/UBSan下でも389 assertionsが成功。Adaと上流libraryは非計測、leak検査は無効。
root拒否、23 ELFの緩和設定、ソース24工程が成功した。
前後source subjectは`392ec4097c9ae170e18e32a6c70c040488855b8295bee8e311e73d51a8a7ed56`で一致。全7repoのproof入力は不変で、新runtimeはSPARK対象外。
展開byteはまだopaqueであり、tar entry・path・link・属性と所有権、全DEB効果、稼働catalogと認可、
実root/boot・完全置換ISO・全言語翻訳は未完として続ける。
[実装境界](distribution/native/deb-data-stream.ja.md)、[検証記録](distribution/evidence/native-transition/deb-data-stream-01/README.ja.md)。


採用11種類のbinary関係項目をnativeで解析し、元DEB観測SDKへ接続した。
項目種別・選択肢group・順序・版条件・architecture labelをprivateな有界式へ保持する。
Providesのarchitecture指定も保持し、ソース保持2項目は厳密な等号版を要求する。
原本と異なるcontrol、不正なbinary折返し・版条件で部分的な観測成功を返さない。
固定環境の全コンパイル・4アプリ・18 Ada main、関係176・メタデータ117・制御229・envelope764 assertionsが成功。
37合成DEBの再生成照合、13元DEB・153項目の独立oracle/CAS照合も成功した。
ISO 09由来statusの2,239パッケージ・4,388関係項目・20,234 atomsが独立Python参照と一致。
これはstatusの関係値の検証で、2,239元DEBの再検査や全依存の充足判定ではない。
二ビルドの22実行ファイルが一致し、397入力を照合した。新経路のroot拒否と22 ELFを確認した。
引数なし試験のrunner末尾空白は共有generatorで修正し、最終runnerで18試験を再実行した。
ソース24工程の前後subjectは`729fca47ca208b682ab2ed7012230f2906a7407eea4d302fd187f355677c5d19`で一致。全7repoのproof入力は不変で、新runtimeはSPARK対象外。
依存充足と全phase・data.tarと所有権・全効果・稼働catalogと認可・実boot・完全置換ISO・全言語翻訳は未完である。
[実装範囲](distribution/native/deb-relations.ja.md)、[検証記録](distribution/evidence/native-transition/deb-relations-01/README.ja.md)。


元DEBからraw controlと原本に束縛した制御項目・識別情報を読むnative SDKを追加した。
未知項目と原本を保持し、単一stanza・UTF-8・重複・必須項目・Source・保護属性を検査する。
通し試験で見つかったstack不足は中間recordをheapへ移して修正し、資源制限は維持した。
固定環境の全コンパイル・4アプリ・17 Ada main、新読取109・制御229・envelope764 assertionsが成功。
35合成DEBの再生成照合、最終binaryによる13元DEB・153項目の独立read-only oracle/CAS照合も成功した。
二ビルドで21実行ファイルが一致し、392入力を照合した。新SDKのroot拒否と21 ELF緩和設定を確認した。
ソース24工程の前後subjectは`156cccf117ef4612a3283ee58341e277889f4de452813df14e28a74152c374ff`で一致。全7repoのproof入力は不変である。
新runtimeはSPARK対象外。依存・任意項目全体・data.tar・全効果・稼働catalogと認可・実boot・
完全置換ISO・全言語翻訳は未完として続ける。
[実装範囲](distribution/native/deb-metadata.ja.md)、[検証記録](distribution/evidence/native-transition/deb-metadata-01/README.ja.md)。


元DEBの制御アーカイブを検査し、通常制御ファイルと属性を既存CASへ保持するSDKを追加した。
未改変のzlib/liblzma/libzstdを使う小さなC境界でstream終端・完全消費・展開量を検査し、
その後にlibarchiveでtarを読む。gzip CRC不正を通してしまう初期構成は試験で検出して修正した。
scriptは元のbyte列として保持し、実行許可や稼働DBは作らない。Cもcanonical索引へ追加した。
最終ソースで全コンパイル・4アプリ・16 Ada main、制御229・envelope764 assertionsが成功。
35合成DEBの再生成、13元DEBの65制御entryの独立ar/Python/CAS照合、三入口のroot拒否も成功。
独立二ビルドの20実行ファイルが一致し、387入力を照合した。C境界のASan/UBSan計測下でも
229 assertionsが成功した。Adaと上流libraryは非計測、leak検査は無効。通常20 ELFの緩和設定も確認。
ソース24工程の前後subjectは`0ac39bc66d1164eb438ac282509f0cd9c43f48ce7625828c3841f810f326c67e`で一致した。
全7repoの既存proof入力は不変。新Ada/C runtimeの形式証明ではない。
[実装境界](distribution/native/deb-control.ja.md)、
[検証記録](distribution/evidence/native-transition/deb-control-01/README.ja.md)。
制御field・data.tar・全効果・稼働catalogと認可・実boot・完全置換ISO・全言語翻訳は未完である。

元DEBのar envelopeと圧縮メンバーを既存CASへ束縛するnative読取SDKを追加した。
原本の全hash・header・順序・サイズを再検査し、保存前に呼出側の全envelopeを照合する。
固定環境でpkgcore全ソース・4アプリ・15 Ada main、新読取器764 assertionsが成功した。
二つの入口のroot拒否と実DEB 7個・全21メンバーの独立ar/CAS照合も成功した。
別パス・入力mtime・TZの新規ビルドで19実行ファイルが一致し、346入力hashを照合した。
ソース24工程の前後subjectは`a1fea042e264bffca34da1d85cac7fea9f495061edd22633009bdbcb72a37945`で一致した。
全7repoのproof入力は不変で、新runtimeはSPARK証明の対象外。
[SDKと残る範囲](distribution/native/deb-container.ja.md)、
[検証記録](distribution/evidence/native-transition/deb-container-01/README.ja.md)。
圧縮tar/control・全効果・稼働catalog・実root/boot・完全置換ISOは未完である。

遅延トリガーの未処理・処理中・待機関係を扱う参照モデルを追加した。
処理中の再発火は別の未処理項目として保持し、受信者が別のパッケージを待つ場合も
待機者を早期解除しない。scope・開始revision・処理名に束縛したattemptで古い応答を拒否する。
checkpointの復号だけでhandlerの再実行・完了を起こさない。
固定環境の配布工具158件（参照状態13件を含む）とソース24工程が成功した。
前後subjectは`30d4b667646dad5a8732fec8a78c109b634d7e319c08680a67834d5b832938d2`で一致した。
[参照状態の範囲](distribution/native/trigger-state.ja.md)と
[検証記録](distribution/evidence/native-transition/trigger-state-01/README.ja.md)。
これは実行器ではなく、成功観測の認証・native CAS/WAL・全package lifecycleは未接続である。

媒体操作を公開コマンドへ接続した。inutocは元DEBを検査して決定的な`.toc`を作り、
installp -l/-Lとgeninstall -Lは原本を再検査して一覧を返す。古い索引や途中変更を拒否し、
索引を導入済みDBや供給認証の代わりに使わない。原本の版・hashを保持する。
固定コンテナで媒体14件を含む142試験と構文検査が成功した。
保存済みの実DEB 7個でも索引の再現性と原本不変を確認した。現在は119メッセージ・7翻訳catalog。
ソース24工程の前後subjectは
`b2b9795aa6de090627c3e742be5dfabc9f408015a5430394dea3e0d871200f53`で一致した。
[媒体の実装範囲](distribution/native/media.ja.md)と
[今回の証跡](distribution/evidence/management-interface/media-01/README.ja.md)。
機械処理の列形式はnative DEB用の開発形式で、完全な応答互換性は未受入。
稼働管理器への接続・全DEB効果・実起動切替・完全置換ISO・全言語翻訳は引き続き未完。

Niaを唯一のパッケージ管理主体とし、内部dpkgバックエンドも採用しない方針を再確認した。
[機能ごとの担当](distribution/native/ownership.ja.md)に従い、systemd等の独立した基盤工具を維持する。
元DEBの6種のトリガー宣言を候補catalogへ保持し、各段階とファイル変更による発火先・待機関係を
有界なデータとして計算する処理を追加した。旧ISOの1,186原本ファイルをhash・サイズ照合して解析した。
handler実行とnative lifecycle/WALは未接続であり、効果完了の判定を緩めていない。
独・西・仏・韓・中国語簡体字・繁体字の訳文を追加し、英語原文115件と7翻訳catalogを検査した。
固定コンテナで128件のnative/hardening/image試験と145件の配布工具試験が成功した。
独立checkoutで失敗していた既存試験のパス参照も修正した。
ソース24工程が成功し、前後のsubjectは
`ef6012e2bbd64da55bc9b012abc15e80acb5b4b9d83564c0d32e36d836365fef`で一致した。
[今回の証跡と残る範囲](distribution/evidence/native-transition/triggers-localization-01/README.ja.md)。
全言語gateは未翻訳を検出して終了値1を維持する。第三者訳文レビュー、GUI・入力の受入も未完。

検査済み世代とcatalogを一つの記録で確定する公開SDKをpkgcoreへ追加した。
全体検査後もstageの二つのlockを保持し、既存CAS/WALと全Managed guardを使用する。
未確定の候補ファイルは現行世代として読まず、進行中は結果不明を返す。
認可・構成署名・barrier・解決証拠の拒否、二世代の更新、途中確定と再開、
欠落・部分journal、候補とaccepted記録の分離を実行試験した。
独立した固定コンテナビルドでpkgcore全ソースのコンパイル、4アプリのリンク、
全14 Ada test mainが成功した。stage試験は1,180、公開試験は333 assertions。
root拒否7入口も使い捨てコンテナで成功した。
作業パス・入力mtime・タイムゾーンを変えた二つの新規ビルドで、4アプリと14試験の
全18実行ファイルがバイト一致した。両ビルドと現行checkoutの343入力hashも一致する。
ソース統合検査24工程が成功し、前後のsubjectは
`16a43c7b1adc304efc51f665283e4de70bf674c915a887556ada5b69262b3253`で一致した。
[設計と残る製品接続](distribution/native/generation-publication.ja.md)、
[実行証跡](distribution/evidence/native-transition/publication-01/README.ja.md)を参照。
これは非特権の論理世代公開SDKで、実mount/boot切替や稼働管理器への接続ではない。
全DEB効果、特権属性、catalog/緊急修正holds意味、本番認可と独立trust floor、
実電源断・容量故障、完全置換の新ISOは未完。
全7コンポーネントの既存proof入力は不変で、新しいruntimeを証明済みとは扱わない。
前段の[分割組立て証跡](distribution/evidence/native-transition/generation-01/README.ja.md)は
元のsource subjectに束縛した記録として保持している。

多言語対応を[設計判断](distribution/docs/decisions/0004-localized-interface.ja.md)に追加した。
Debian 13のglibc全509 locale/encoding組とinstaller 78選択肢を対象として固定し、
文字体系・地域の変種を保持して検索する。公開12コマンドの表示層はgettextを使用し、
初回に英語原文と日本語訳115件を実装した。初回の固定コンテナの工具試験127件、実HTTPSの
公開コマンド試験6項目とソース検査24工程が成功した。ソース検査前後のsubjectは
`8d7624f4932cced4741fae446ceb6d1fc3fd7456be3892734bffdac345ddaef1`で一致した。
全言語の訳文、TUI/GUI、font/shaping/入力とアクセシビリティは未完である。
全言語release gateは未翻訳を検出して終了値1となる。fallbackを翻訳完了と数えない。
[多言語の検証記録](distribution/evidence/management-interface/localization-01/README.ja.md)。

公開操作は[管理コマンドの最新判断](distribution/docs/decisions/0003-management-interface.ja.md)へ変更した。
外部のsystemd等は元の操作体系を維持する。Niaの12コマンドの引数解析と、
原本DEBに対応するアップロード緊急度・DSA/CVEの修正ソース版識別を追加した。
元DEBを改変しないnative緊急修正成果物の作成・読取をepkg/emgrへ接続した。
共有の供給認証に上流TUFを採用し、`emgr_download_ifix`へ実HTTPS取得を接続した。
署名・委譲・鍵交代・期限・metadata版と参照hashを検査し、信頼cacheを原子的に保存する。
前回の供給認証検証では固定Debian 13コンテナの試験が111件成功（native 91、hardening 4、image 16）。
別の使い捨てrootコンテナで実公開コマンドの結合試験4項目も成功した。
ソース検査24工程も成功し、前後のsource subjectは
`05eefe705d9265ec11e71181f0b90ba5dfcb14ed0e55758b174f53394b0a7876`で一致した。
[供給認証の設計](distribution/native/repository.ja.md)と
[検証記録](distribution/evidence/management-interface/repository-01/README.ja.md)を参照。
[追加調査](distribution/native/command-review.ja.md)では作成・比較・媒体コピー・検索・
ライセンス・権限・診断等の抜けを整理した。台帳121名称は全コマンドの採用完了を意味しない。
公開管理器、emgrの適用・削除・保留、本番の鍵・信頼policy配備、契約の意味検証、対話画面の実接続、
旧公開niaの配布廃止と新ISO受入は未完。名称の修正は自作ソース・説明が対象で、
過去の原本メタデータや証跡は維持した。Adaの数学的入力は変更していない。

APT/dpkgを恒久採用する方針を利用者の明示指示で変更した。
[最新判断](distribution/docs/decisions/0002-native-package-authority.ja.md)に従い、Niaを唯一のwriterにする。
下記のISO 09とその証跡はAPT基準版の実績であり、完全置換の成功を意味しない。

完成ISOから抽出した2,239パッケージのstatusと8,959個のcontrolファイルを検査・hash照合した。
1,493パッケージに計2,263個の保持された効果ファイルがある。管理器関連11パッケージの
仮除外で元の依存12条件が未充足になる。原本DEBの全effect/phase変換、実root/catalog公開、
Nia自動更新とGUI、更新・障害復旧の受入は未完。[工程](distribution/native/README.ja.md)。

[ハードニング基準と検査工具](distribution/hardening/README.ja.md)を追加した。
既存Niaの全18 ELFでPIE/NX stack/RELRO/NOW/非RWX LOADを実確認した。
新しいrootfs設定の本番組込み・起動早期適用・実機受入は別工程として扱う。

ハードニングのLive BIOS/UEFI/Secure Boot 3試験が成功し、日本語入力・保存、Firefox起動、
DNS、user namespaceを確認した。Nia観測器のAppArmor profileと制限付きloaderを追加し、
読取・書込・network・execの拒否を実測した。別の試験ディスク差分では、設定保存後の
Secure Boot再起動で全30検査とservice自動起動が成功した。元ディスクのhashは不変。
[証跡](distribution/evidence/hardening/desktop-01/README.ja.md)。
これは旧APT基準版に対する隔離された試験であり、新しいNia-only ISOの受入ではない。

前回のソース検査は24工程が成功し、前後のsource subjectは
`1bc2cabd078faad3fae822713fca2f8d06ee74436f2fe458700549e54203bd4f`で一致した。
image/native/hardening工具の25試験も成功。7コンポーネントのAdaソースとGPRは変更しておらず、
以前の形式証明を新しいPython工具やAppArmor設定の証明と扱わない。

コンポーネント受入時（workspace commit `baba69f`）のsource subjectは`2d5b48e6fa437795af02df4943ea1b365ddad62185a88a5d394d201a45958c3d`。固定コンテナでのnative受入と、全7コンポーネントの厳格なSPARK flow・全体証明を完了した。

その後、利用者の指示によりDebian 13の実配布構築へ進んだ。新しいビルド工具・パッケージングは[配布構築手順](distribution/image/README.ja.md)、従来の独自カタログモデルとの関係は[設計判断](distribution/docs/decisions/0001-debian13.ja.md)。コンポーネントの証明と、次のISO受入を別々に記録する。

## Debian 13の実イメージ

`niaos-0.1.0-amd64.hybrid.iso`（3,637,100,544 bytes）のSHA-256は`d4c18dc0e2be653bf11a04db40db95ca0353322010133e068dda274bd4aa314b`。KDEの実Live環境でBIOS・UEFI・Secure Boot、日本語の実入力と保存を確認した。新規仮想ディスクへのUEFIオフライン導入、BIOSオンライン導入、それぞれの再起動と導入済みディスクのSecure Bootも成功した。Liveとオンライン導入先で、通常Debianミラーの署名付きAPT索引を実取得した。[6項目の一括受入と構築記録](distribution/evidence/debian13/accepted-09/README.ja.md)。

上流kernel・systemd・KDE・live-build・Debian Installerと、既存7コンポーネントのソースは改変していない。独自DEB、正式なchroot hook、KConfig、APT/GRUB設定の追加で統合する。試作で見つかった識別情報、Wayland日本語入力、bootstrapのCA証明書、インストーラーのHTTPS親ミラーとミラー設定モジュールの問題を配布レシピで修正した。失敗・中断記録も[evidence/debian13](distribution/evidence/debian13/)に残す。

独自DEBの構築で58 Ada mainを実行し、再ビルドした19 DEB（デバッグ情報を含む）と8組16ファイルのnative source packageが全件一致した。同一入力からの独立した2回のISO構築でも、SHA-256と実バイト列が一致した。[09/10比較](distribution/evidence/debian13/reproducibility-09-10/README.ja.md)。対応ソース1,415組・4,667ファイル（8,524,077,623 bytes）を保管し、内蔵インストーラー用Linux本体の補完とホスト側での全ファイル照合も完了した。[ソース記録](distribution/evidence/debian13/accepted-09/source-collection/README.ja.md)。GitHub ActionsのDEB構築workflowも用意したが、GitHub上では未実行。

オフライン導入で「ミラーを使わない」を選ぶとCDソースだけを保持する。オンライン導入は通常ミラーを設定する。実機のGPU・音声・無線・サスペンド、暗号化導入、対話GUIの全操作、GNOME/serverイメージは未受入。Live終了時の読み取り専用メディアのunmount警告も実ログに保持する。

配布工程後の[ソース検査](distribution/evidence/debian13/accepted-09/source-check/README.ja.md)も全24工程が成功した。対象source subjectは`35f0072871a19fb269111dc4727428968b9bb0c3418a63a31840a4fbaa273acf`。既存コンポーネントのビルド・証明対象とは分けて記録する。

## 実コンパイル・実行試験・再現性

固定したDebian 13.6 amd64 imageと2026-09-07の署名済みsnapshotで、全499正本Adaファイルをコンパイルし、18 CLIをリンク、全58登録Ada mainを実行した。統合103項目が成功し、実行前後のsource subjectは一致した。Python参照・工具・プロトコル試験555件は、通常実行の544件と、別contextのroot拒否1件・私有D-Bus10件を合わせて成功した。

署名付きDEB人工fixtureのGPG依存不足を修正した。現在はgpg・gpg-agent・gpgconf・gpgv・dpkg-debを必須とし、不足時は統合検査を開始前に失敗させる。今回の固定コンテナでは当該fixtureの省略はない。root拒否試験はGitHub Actionsでも専用コンテナで実行する設定を加えた。GitHub上での実行自体はまだ行っていない。

異なる長さの作業パス、入力mtime、JOBS=1/2、UTC0/HST10で2回ビルドし、18実行ファイルがデバッグ情報込みで完全一致した。また、各コンポーネントを兄弟repoなしで別々にmountし、全7repoのcompile-all・build・testを実行して成功した。以前のビルド生成物は持ち込んでいない。

[固定コンテナ受入の概要](assurance/evidence/native-development/current-fixed-container/report.json)、[全native検査](assurance/evidence/native-development/current-fixed-container/native/report.json)、[再現性](assurance/evidence/native-development/current-fixed-container/reproducibility/report.json)、[独立ビルドを含む実行一覧](assurance/evidence/native-development/current-fixed-container/pipeline-report.json)を保存している。CIとroot試験の説明だけを受入後に追加した差分は[別記録](assurance/evidence/native-development/current-fixed-container/post-run-workspace-changes.json)にある。コンポーネント・ビルド・工具・package入力は変更していない。

## SPARKの証明

GNATprove 16.1をchecksumで固定し、全unit対象の厳格なflowとlevel 4 proveを使う。未証明・警告は失敗にする。次の件数は各repoの固定vendorも含むため重複する。

| コンポーネント | 全体証明 |
| --- | ---: |
| assurance | 1,809項目 成功 |
| pkgcore | 3,943項目 成功 |
| statecore | 3,592項目 成功 |
| controlcore | 2,030項目 成功 |
| configcore | 2,292項目 成功 |
| resolvercore | 2,499項目 成功 |
| capsulecore | 2,135項目 成功 |

全7repoについて、現在の数学的入力集合と完了実行の集合が完全一致することを確認している。pkgcoreの実行時workspace subjectは`091ce3fc…`、assurance・statecore・controlcore・configcore・resolvercoreは`330e7a97…`、最後に修正したCapsuleは現在のsubjectである。文書や試験工具の依存変更だけを理由に、同じ証明を重複実行していない。[全7repoの照合結果と完全な実行証跡](assurance/evidence/native-development/current-component-proof/report.json)を保存した。中断したworkspaceコマンドを成功に置き換えず、完了した各repoの結果を照合している。

Capsuleの前回の全体実行では、権限の積集合とpromptの書込位置に10件の未証明が残った。点ごとの積集合・Subsetの契約、容量とcursor進行の契約・不変条件を追加した。選択範囲61項目の厳格証明に続き、全能力の16組合せ、最小・最大長の独立digest基準値、高い配列添字、無効入力のAda試験を通過し、最後の全体証明も成功した。途中の[選択証明と実行試験](assurance/evidence/native-development/scoped-capsule-bounds-20260908/report.json)は、全体証明と分けて保存している。

State_Cluster_Safetyの自動展開中のツール内部エラーも保存し、旧・新両構成の過半数を維持するループ不変条件を追加した。その後のstatecore全体証明は成功している。修正と互換性の理由は[ADR-0053](assurance/docs/engineering/adr/ADR-0053.ja.md)。

## 開発環境とGit管理

7コンポーネントとdistributionは独立Git履歴を持ち、workspaceがsubmoduleのcommitを固定する。固定vendor・profile・人工fixture・独立CI/test runnerは正本から再生成する。手順は[開発環境](dev/README.ja.md)と[公開手順](dev/PUBLISHING.ja.md)。

高負荷による強制再起動を受け、重い検証は1件ずつ実行する。ローカルは一時user scopeでメモリ3 GiB・swapなし・CPU 1コア分・128プロセスをkernelで制限し、実行前に読み戻す。固定コンテナ内部からも同じ値を確認した。証明はさらに単一起動lock、子孫監視・回収、プロセスごとの上限、実時間上限を適用する。上限到達を成功にしない。詳細は[ADR-0054](assurance/docs/engineering/adr/ADR-0054.ja.md)。

## 製品開発として残るもの

Capsule launcherのpidfd/cgroup/LSMによる実本人確認、native portalと資源のIssue/Withdraw、独立anchor、実GTK/KDE表示とsession切替、kernel sandbox、Flatpak closure、microVM、GPU/Steamの統合は未完。SDK callbackを常にOKで埋めて完成扱いにしない。

研究モデルのfull root/catalog-WAL、独自DEB意味層、独立rescue、UKI署名起動、remote management HA、physical fencing、実DB復元、独立trust floor、安全な長期GCは別の製品開発と受入試験が必要。今回のDebian経路ではAPT/dpkgとDebian Installerを採用し、研究モデルの独自executorを有効化しない。既存の[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)は、この独自機能群の未完条件として維持する。

GitHubへのremote設定とpushは未実施。公開先が決まれば[公開手順](dev/PUBLISHING.ja.md)で独立repoを先に、workspaceを後に公開する。
