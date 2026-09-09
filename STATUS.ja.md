# Nia OS 開発・配布検証状況

2026-09-09。Debian 13ベースの起動・導入可能なKDE開発版。実ISOのVM受入を完了し、既存コンポーネントの実コンパイル、実行試験、再現性、独立Git管理も整備した。本番認定・実機認定は行っていない。

## 最新依頼: Niaへの完全置換とハードニング

### 直近の検証

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
