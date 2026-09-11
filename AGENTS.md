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

2026-09-11 UTC。設定済み世代の論理的公開と、受理済み記録の復旧を接続した。
NIAGEN06の新規公開と未受理の再開は、stage検査と公開engineの実CAS予約の両方で現在の設定元を照合する。
Observe_Configuration_Sourceは既定拒否で、独立認可と操作全体のsource排他を要求する。
active transactionだけでは現在照合を省略しない。受理済みの同一state/plan/catalogと完全なjournalだけが、
別型Retained_Generationを使ったfinish-terminal処理へ進める。全物理stage/保持閉包/pin/receiptと現在認可を維持する。
古いsource FDがなくても元health receiptと全after-imageを確認して記録を修復し、新しい公開決定や設定適用を行わない。

固定環境で3 mainを強制compileした。設定済み公開251、新規/activeの検査後source変更95/125 assertionが成功。
新プロセスでのaccepted再開と、設定record/閉包/物理tar/stage journal/publication journal/pinの6欠落拒否も成功。
旧v4公開2,023、v5公開142、stage1,211、設定済み世代358 assertionと、現在観測13 case、独立6 root、公開oracleも成功。
最終のAPI説明comment訂正後にも3 mainを強制compileし、実行済みbinaryとの完全一致を確認した。
最初のPython oracleのtar path表記とADR必須見出しの不足を修正し、失敗ログも保存した。
401 compile入力、41 fixture、8 Python工具を正本へ照合し、構造/link/lint/license/生成CIが成功した。
Ada mainは83。共有vendor/数学的入力とworker/serviceは不変で、全suite/証明/旧カオス/VMは反復していない。
3 GiB/swap0/CPU1/pids128で順次実行し、全job終了済み。component/統合CIへ新wrapperを登録した。
subjectはab72f448d25ce2e710d147ebb65a076f6062d2fa3d8298e898de7f7e0d30809f。
判断ADR-0109、証跡distribution/evidence/native-transition/configured-publication-01/（65 file、SHA256SUMS込み）。
私有labはnative-configured-publication-01。最新3 mainのbuild cacheはここに保持する。

利用者の追加依頼で未使用VM/旧ISO等48 fileと過去build cache105 directoryを削除し、約12.16 GiBを解放した。
空き容量は約4 GBから17 GB、使用率99%から93%。保持するqcow2のbacking関係とQEMU停止を確認した。
Distroboxから一部host FDは列挙できず、可視FDと完了済み私有出力の範囲で確認した。完全なhost FD検査とはしない。
最新ISO 09、二つの受入installed VM、builder/base、対応source、全sourceとsealed evidenceを保持した。
過去labのbuild cacheと使い捨てVM差分は消えているため、過去のパスにbinaryがあると仮定しない。
整理記録はdistribution/evidence/maintenance/storage-cleanup-20260911/。

GitHubのminto-dane認証を確認したが、既存minto-dane/niaosは別の非公開kernel projectだった。
上書きせず、workspace候補をniaos-distributionとしてdev/PUBLISHING.ja.mdへ記録した。
repo作成/push/release/remote CIは未実施。利用者による実施許可は継続して有効である。

次は抽出済みfilesystemの完全検査と、実root/boot切替へのbinding・段階別復旧を接続する。
今回のacceptedは保持archiveを選ぶ論理的SDKのstateであり、稼働rootやbootの資格ではない。
本番source/consent/quiescence provider、実物の検査とmount identity移行、世代GC、全DEB効果、
本番認証UI、完全置換ISOと全言語翻訳も未完。fixture認可を本番へ配備せず、属性検査を緩めない。

以下は前工程の記録である。

2026-09-11 UTC。設定済みrootを世代保持・格納・実準備へ接続した。
NIAGEN06は320 byte headerで元NIAROOT1/2に加えてNIACRT01/NIACRC01を明示的に束縛する。
保存設定の元root/catalog/closure、intentのroot/architecture、世代transaction、Context=Intentを照合する。
既存pinを使用し、v1..v5のwire/transactionは維持した。GC走査の実装は別途必要である。

Pkg_Generation_Stageへ既定拒否のObserve_Configurationを追加した。独立に認可された設定元FDを借用し、
操作全体のsource排他をproviderへ要求する。通常Verify_Currentをprovision/advance/inspect/準備へ接続し、
内側engineがCASを取得する二箇所でもCheck_Inputsから再観測する。元Authorizeも全effectで維持する。
Prepare_Rootは設定済みtar FDと実CAS予約FDを既存サービスへ渡し、応答後も保存内容/source/認可を確認する。

固定環境で4 mainを強制compileした。最終の設定済み世代358 assertion、現在観測13 case、独立6 rootが成功。
元root831、既存stage 1,211、旧v5公開142 assertionと独立公開oracleも成功した。
最初の旧root/stage実行後に追加したv6専用test helper差分はbefore-source-checkとtest-01-inputsに保持した。
本体runtimeは全実行で同じ。最終helperを使う2 mainを再compileし、設定済み試験を実行した。

使い捨てVMの実サービス/workerで2 case（各367 assertion）が成功した。空のlocal設定とvendor退避、
世代wire/保存scope/送信tarを照合し、展開後認可拒否はIndeterminateで非公開のextracted rootを保持した。
VM 01のfixture作成権限、VM 02の媒体directory権限を修正し、VM 03が成功した。媒体検査は維持した。
追加試験のFD型取り違えと梱包用worker hashの取り違えもログを残して修正した。
開発用workerの実hashはed188c4f23f9078ecaecfff829de6f4a53ba533f0a36a77c6189d5a09a9a123d。
配布パッケージの別binary 6518709d…と混同しない。worker sourceとbytesは前の受入から不変である。

401 compile入力、32 fixture、9 Python工具、4 worker sourceを照合し、構造/link/lint/license/生成CIも成功。
Ada mainは83。共有vendor/数学的入力は不変。全suite/証明/旧カオス/性能campaignは反復していない。
3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPUを維持し、全job終了済み。GitHub公開は未実施。
subjectはd46d244395105b30d2571a84ed87524b39e3f94704efd9dcaae2a896ba00d267。
判断ADR-0108、証跡distribution/evidence/native-transition/configured-generation-01/、私有lab native-configured-generation-01。

次は設定済み世代の公開・accepted復旧を接続する。publisherの既存v4/v5制限は維持し、v6公開はUnsupported。
適用前sourceの現在照合を、設定適用後やboot後の状態へ無条件に流用してはならない。
実物の再検証と段階別の復旧根拠、本番source/authentication/quiescence provider、mount identity移行が必要である。
このfixtureのsource providerや供給鍵を本番配備せず、稼働rootの属性チェックを緩めない。
世代GC、全DEB効果、本番provider/認証UI、実root/boot、完全置換ISOと全言語翻訳は未完である。

以下は前工程の記録である。

2026-09-11 UTC。CAS予約を取り直した後の設定再観測と全root照合を実装した。
Pkg_Conffile_Choice.Reobserveは保存memberを先に検査し、現在のrootから原本/宣言・inode/属性/内容・
退避先を通常のPrepare/Resolveで再観測する。新規観測の期限とそのrecord参照だけを除いて全byteを比較し、
保存choice閉包を現在のsourceから厳密に導出する。sourceとrecordの役割を区別して保持し、digestが同じでも
必要なsourceを消さない。返すのは現在の予約に属する新sessionで、旧proposal/期限/hashを変更しない。

Pkg_Configured_Root.Verify_Currentは保存閉包と独立期待bindingを検査し、全choiceを再観測して通常Buildへ渡す。
元所有権・配置・prefix/content・完全tarとmanifestを照合し、最後に全新choiceをlive確認する。
保存結果のarchiveだけを返す。新規観測/派生の未pin CAS objectは残り得る。
観測期限は同意・失効・新規要求や復旧の許可を更新しない。root FD/scopeと保存選択の認可は別途必要である。

固定環境で対象2 mainを強制compileし、設定選択297 assertion（9経路の新規再観測を追加）、全root192 assertionが成功。
新プロセスで現在の空fileと過去5観測を区別し、構造上は読めるownership/prefix/root byteの不整合を
全root照合では拒否した。旧期限1の再観測も、現在の条件が一致するときだけ成功した。計13 caseが成功。
過去の全CAS memberは元hashを維持した。独立した元6 rootの原本span/閉包照合と保存参照35 caseも成功。
同じmount namespaceでのプロセス再起動の受入であり、OS再起動時のidentity移行・適用後の復旧認定ではない。

初回はテストhelperのFD型演算の可視性でcompile停止し、修正後test-02.logで全対象が成功した。
API説明comment更新後にも対象を強制compileし、compile-03.logで実行済みroot binaryとのbyte一致を確認した。
そのbinaryは44df0a7061e8c92dc381e4fb5f450a074f9e1dcf1e3b720c5dc7437a89a062a0。
399 compile入力・26不変fixture・7 Python工具を照合し、構造/link/lint/licenseと生成CIも成功。
新current oracleは標準component CI/統合runnerで元driverと同じmount namespace内に接続した。
Ada mainは83。共有vendor/数学的入力、workerとfixtureは不変で、全suite/証明/旧カオス/VMを反復していない。
3 GiB/swap0/CPU1/pids128。全job終了済み。GitHub公開は未実施。

subjectは972bb968e5f4def48ad3496808add2ede374315cc2e6c1266fc82ab0661d9b19。
判断ADR-0107、証跡distribution/evidence/native-transition/configured-current-01/、私有lab native-configured-current-01。

次は世代形式へ設定済みmanifest/closureと期待scopeを明示的に束縛し、世代pinと各stage/公開phaseへ
新規観測を接続する。既存NIAGEN05のroot欄を暗黙に新形式へ拡張しない。
このAPIを呼べることを、本番の期待root FD/scope/同意の認可や、既存公開経路への接続完了にしない。
mount/inode identity移行、accepted状態の復旧、世代GC、全DEB効果、本番provider/認証UI、実root/boot、
完全置換ISOと全言語翻訳などは未完である。

以下は完了済みの前工程である。

2026-09-11 UTC。設定済みrootの保存参照loaderを実装し、live Verifyの先行検査へ接続した。
Pkg_Configured_Root_Record.Loadは新プロセスから同じCASを読取専用で開き、全member/hash、
元root/catalog/選択のbinding、件数・順序・サイズ、宣言閉包と生成物のexactな和集合を検査する。
全binding/choice/設定entry/memberをViewから列挙でき、削除の選択も残す。失敗時はViewを消す。
保存物を再生成せず、旧proposalをlive状態へ復活させない。新しい期限は読込だけに適用する。
既存Verifyはその後もlive配置・所有権・全選択とBuild結果の完全一致を検査する。

固定環境の対象main強制compileと既存190 assertionが成功した。独立Pythonによる元6 rootの
原本span/選択/保持集合の照合も成功した。新プロセスの最終35 caseで、6 rootの全返却field、
不整合・scope・件数/配置/サイズ・保持集合の過不足/順序と10種類の保存object欠落を検査した。
旧期限1の記録も履歴として読めることを確認した。全読込前後でCAS object集合/内容が不変で、
欠落は未修復のまま残る。有限期限とgetter/失敗時出力消去も確認した。
プロセス再起動の試験であり、認証済み復旧適用や実bootの試験ではない。

初回compileのByte演算可視性不足を修正し、test-02.logで成功した。
保存記録34 case成功後に旧期限のcaseを追加し、最終oracle-02.logで35 caseが成功した。
399 compile入力・26既存fixture・6 Python工具を現行ソースと照合した。
標準component CIと統合runnerへ保存記録oracleを接続し、構造/link/lint/licenseと生成CIの検査も成功。
共有vendor/数学的入力、特権workerとfixtureは不変。全suite/証明/旧カオス/VMは反復していない。
Ada mainは83。3 GiB/swap0/CPU1/pids128を維持し、全job終了済み。GitHub公開は未実施。

subjectは78bfa9040cd90d8374765d1fc20dd46224aad6792e60c11935e099537e45baa0。
判断ADR-0106、証跡distribution/evidence/native-transition/configured-record-01/、私有lab native-configured-record-01。

次は設定済み形式を世代の保持・実root準備・公開経路へ明示的に接続する。
Loadの保存参照整合性だけを原本由来の閉包完全性・所有権/配置の意味検証・同意・GC/実行許可にしない。
後段の期待digest/scope認証、live選択と本番admission、認証済み復旧、世代pin/GCは未完。
全過去設定/隠れた属性/全inode/DEB効果、本番provider/認証UI、実root/boot、完全置換ISO、全言語翻訳も未完。

以下は完了済みの前工程である。

2026-09-11 UTC。設定済み全rootのstream生成と保持記録を実装した。
Pkg_Configured_Root.Buildは配置/所有権/全選択を再検証し、未変更の原本spanと設定prefix/contentを
64 KiB bufferで完全tarへ出力する。root/親とhardlink依存を保ち、削除/退避と空fileを区別する。
NIACRT01に元binding・root/transaction/context・architecture・全choice・prefix/content・出力を記録する。
NIACRC01はcatalog/choice閉包と元/生成物のexactな和集合を保存し、返却前に全choiceをlive再確認する。
Verifyは全保持memberを先に検査し、欠損を黙って再生成しない。明示Buildによる再構築とは区別する。

固定環境で対象mainを強制compileし、既存配置を含む190 assertionが成功した。
独立Pythonでローカル保持/vendor採用/普通のlink chain/削除/復元/空fileの6 rootについて、
原本span・属性/内容・全選択binding・保持集合の過不足を照合した。保存root欠落、明示再構築の同一性、
容量/期限/context/live変更の拒否も確認した。65,537 byteの原本本文でstream境界とpaddingを通した。
使い捨てVMで同じ6 root（計26 entry）を専用ext4へ展開し、最終namespace、元/設定内容、
mode/UID/GID/mtimeと明示atime、設定xattr/flags・hardlinkを照合した。拡張ACLは前工程の別受入である。

初回174 assertion成功後に故障/境界caseを追加し、最終test-02.logで190 assertionが成功した。
独立oracleを標準component CIと統合runnerへ接続した。固定環境でも同じ6 caseのoracleが成功。
既存24 DEB fixtureはbyte不変、新しいlayout-streamだけを追加し、25 DEB+manifestを再生成照合した。
395 compile入力・26 fixture入力・12 Python/worker入力を照合し、構造/link/lint/licenseと生成CIも成功。
特権worker sourceは不変で、今回の固定buildも前工程の私有buildとbyte一致した。
共有vendor/数学的入力は不変、全suite/証明/旧カオスは反復していない。Ada mainは83。

subjectは77aeec4ab488bbcb6fcc0fd3e9e1becc45ed0376b5ec75b2fbd7faa46dee33d6。
判断ADR-0105、証跡distribution/evidence/native-transition/configured-root-01/、私有lab native-configured-root-01。
3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPU。全job終了済み。GitHub公開は未実施。

次は新しい設定済みrecordを世代の保持・実root準備・公開経路へ明示的に接続する。
Verifyはlive proposalを必要とし、durable復旧loader・世代pin/GCへの接続は未完。
全過去設定、隠れた属性/全inode/DEB効果、本番provider/認証UI、実root/boot・復旧、完全置換ISO、
全言語翻訳等の全体要件も未完。生成物の保存を本番認可・起動切替の成功に置き換えない。

以下は完了済みの前工程である。

2026-09-10 UTC。保存済み設定属性を通常fileのtar prefixへ変換するPkg_Configuration_Entryを実装した。
NIACOBS1/元DEBから内容・数値mode/UID/GID・ACL/xattr・flags・4時刻を再観測する。
vendor permission overrideは元pathのローカル観測へ束縛し、named ACL権限を残してowner/group-class/otherを変更する。
未知active属性、範囲外named ACL ID、未解決のローカル複数link、原本/assertion不整合や期限切れは出力を消して拒否する。

独立native読戻しでACL_GROUP_OBJとACL_MASKの混同によるmode差を検出した。
SDKの数値modeと実展開workerのstat照合を修正し、元group-owner ACLを改変せずmaskと区別する。
上流ソースは変更していない。誤ったmodeを含む旧派生metadataは再観測結果が変わるため、
旧hash/原本の暗黙書換えは行わない。対象旧計画の移行・復旧受入は未認定である。

対象Ada mainを強制compileし、設定観測/変換141、tar出力83、既存payload814、root archive831、設定配置136 assertionが成功。
ローカル保持/backup/vendor/権限継承vendorの4経路を独立NIACOBS1/DEB読取とnative payload各26 assertionで照合した。
同じ4経路のoracle起動を標準component CIと統合runnerへ接続した。
root-preparation 0.2.2の2 build directoryで主DEB/dbgsymがbyte一致し、導入済みworkerで既存7 caseが成功した。
隔離VMの専用ext4でも4経路の内容・権限/所有者・ACL/xattr・flags・実mtime/atimeが一致した。
ctime/birthtimeの任意復元、全FS範囲、実bootの認定ではない。

初回compile可視性・fixture相対path、独立観測decoderのtag幅、ACL mode差、VM工具PATH・再起動時/tmp消失を検出した。
修正後の最終設定実行はtest-04.log/roundtrip-04.log、実FSはvm-entry-03。途中ログを保持した。
393 compile入力・72 fixture・6 Python工具・23 package入力を照合し、構造/link/lint/licenseと生成CIも成功。
Ada mainは83。共有vendor/数学的入力は不変で全suite/証明/旧カオスは反復していない。

subjectは0333e6374ca54ea9e37b9c29f009b3cf78f7ee536668cb3af975248ecea1b115。
判断ADR-0104、証跡distribution/evidence/native-transition/configuration-entry-01/、私有lab native-configuration-entry-01。
3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPU。全job終了済み。GitHub公開は未実施。

次は設定済み全root stream/CAS保存と、全prefix/選択/原本の保持・live再検証への接続である。
全過去設定、隠れた属性と全inode/DEB効果、特権observer、本番provider/認証UI、旧計画移行・保持/復旧・実root/boot、
完全置換ISO、全言語翻訳などの全体要件は未完。prefix変換とVM fixtureを製品接続完了扱いしない。

以下は完了済みの前工程である。

2026-09-10 UTC。root生成と実展開の親子順の不一致を修正した。
BuildはNIAROOT2を生成し、directoryをcanonical raw path順でroot・親・子の順に出力する。
その他の原本順とhardlink依存、元のheader/拡張/body/paddingは保持する。
NIAROOT1のVerify/Verify_Targetは従来のbyteで照合する。Verify_Ownershipは旧形式にも実展開順を要求し、
不適切な旧順をUnsupported・両digest zeroで拒否する。適切な旧順は受理し、暗黙移行や既存hash変更をしない。

Debian 13で対象3 mainを強制compileし、root archive 831、設定配置136、root公開variant142 assertionが成功した。
二つの逆順directory原本からroot/親/子の採用元を8通り選び、独立Pythonで全原本span・親/リンク順・
旧byteを照合した。共有属性が同じなので8通りの出力tarは同一である。その同一性を検査して実展開を1回に絞り、
VMで11 entryのroot/親先行、数値属性、内容、負nanosecond時刻、hardlink chainを確認した。
既存13 pathの原本spanと、10 pathの実stage/論理公開状態の独立oracleも成功した。実bootではない。

初回CAS directory権限、tar directory名の末尾slash期待値、再実行でのtest stage名衝突を検出した。
試験器と実行先を修正し、途中ログを残した。最終root検査はtest-04.log、回帰はregression-01.log。
390 compile入力・37 fixture入力・6 Python工具を照合し、二fixture集合各5 DEBの再現性も確認した。
標準component CIと統合runnerへ新しい独立order oracleを接続した。構造/link/lint/licenseと生成CIが成功。
Ada mainは83。数学的入力/共有vendorとworker本体は不変で、全suite/証明/旧カオス・worker再buildは反復していない。

subjectはcbc8eb5c0fa7511cb5a17e7f593cb27f5d5c363e683d3203b174d621ca94c56e。
判断ADR-0103、証跡distribution/evidence/native-transition/root-order-01/、私有lab native-root-order-01。
3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPU。全job終了済み。GitHub公開は未実施。

設定を含む全root直列化へ接続する前提の修正であり、元属性adapter/設定済みtar stream・CAS保存はまだ未完。
全属性とinode/link効果、全過去設定、特権observer、認証UIと全managed認可、保持/復旧・実root/boot、
残る全DEB効果、完全置換ISO、全言語翻訳等を引き続き実装する。

以下は完了済みの前工程である。

2026-09-10 UTC。root workerへ原本tarの時刻を読む独立cursorを接続した。
負の小数/負zeroをPOSIX timespecへ正しく変換し、実展開前と照合前の両方へ適用する。
rootの最終時刻も補正する。checksum、entry種別/size、拡張の長さ/重複、padding/終端と期限を検査する。
元FDのoffsetを変えず、可変metadataの全entry保持や上流ソース変更は行わない。

独立wire 34 caseと同じ34 caseのASan/UBSan検査が成功した。
Debian 13の使い捨てVMで正/負のroot各10 entryと5拒否caseが成功し、root/dir/file/symlink/hardlinkの
実mtime/atimeを独立した整数nanosecondと照合した。既存owner/mode/ACL/xattr/内容/raw名と全inode種別も確認した。
新しい0.2.1ソースpackageへhelperと標準試験を含め、別directoryの主DEB/dbgsymがbyte一致した。
導入したworkerでも同じ7 caseが成功し、socketの自動起動/有効化がないことを確認した。
wireの全signed境界をFSの全範囲復元保証にせず、ctime/birthtimeの任意復元も主張しない。

初回VMはDistroboxのUID0によるKVMアクセス拒否で停止し、通常userで起動した。
初回package比較は試験器の古い0.1.0ファイル名で停止した。build自体は0.2.0で成功しており、
最終0.2.1のbuild/比較/導入を別VMで完了した。途中ログを保存し、成功結果へ置換していない。
7 worker入力と23 package入力を現行ソースと照合した。構造/link/lint/licenseと生成CIも成功。
Ada/数学的入力・共有vendorは不変で、全suite/証明/旧カオスは反復していない。全job終了済み。

subjectは4230d1d819551dc90354ad75318b0e962963e2659f29a4b9a5a00739311f6d1f。
判断ADR-0102、証跡distribution/evidence/native-transition/root-clocks-01/、私有lab native-root-clocks-01。
3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPUを維持した。GitHub公開は未実施。

次は元属性adapter/全root配置からのtar stream・CAS保存への接続である。
全属性とinode/link効果、全過去設定、特権observer、認証UIと全managed認可、世代保持/復旧・実root/boot、
残る全DEB効果、完全置換ISO、全言語翻訳等の全体要件も未完である。

以下は完了済みの前工程である。

2026-09-10 UTC。通常設定fileのPAX/header出力codecを追加した。raw名、全permission bit/数値owner、
全signed nanosecond時刻と拡張fieldを保持する。raw xattrはLIBARCHIVE形式に変換し、BINARY名、
encoded key/base64、全signed端点をnative framingで検査する。拡張の予約field上書き・重複を拒否し、
失敗時はbuilder/出力を消す。prefix出力であり、全rootの直列化・実属性適用は未接続。

Debian 13の対象2 main強制compileで出力79 assertion、既存payload814 assertionが成功した。
生成tar 2個を独立Pythonで読み、scriptなしDEBへ包んでnative payload各26 assertionと
Pythonの内容/hash/全時刻/raw xattr/ACL/flags照合を通した。386 compile、41既存fixture、2interop入力が一致。
初回compileのsigned演算可視性と、SCHILY encoded名の不一致を検出・修正し、途中ログも保存した。
新規raw属性出力にLIBARCHIVE形式を使い、既存SCHILY入力の解釈は変更していない。
構造/link/lint/licenseと生成CIも成功。Ada mainは83、数学的入力/共有vendorは不変。
全suite/証明/旧カオス/VMは反復していない。全job終了済み。

固定libarchive 3.7.4 writerで負の小数時刻の相違と指定birthtimeの省略を確認した。
新codecは正しく出力する。一方、直接upstream readerの時刻値にも相違があり、native payloadは既存の
framing補正で一致するが、root_extract.cは現在upstream entry時刻を直接使う。この実適用側の補正は未完。
旧workerの自己読取/自己比較を負の小数時刻の正しさの証拠にしない。probeの原本/ログを保持した。

subjectは74b1d80006cd2fb2638b165826ba4407a28a0a15cc6290742bc7dc3ab3933d22。
判断ADR-0101、証跡distribution/evidence/native-transition/configured-tar-01/、
私有lab native-configured-tar-01、最終test-04.log。3 GiB/swap0/CPU1/pids128、強制-fを維持した。
GitHub公開は未実施。

次は実展開workerのcanonical時刻補正と、元属性adapter/全root配置からのtar stream・CAS保存への接続。
全属性とinode/link効果、全過去設定、特権observer、認証UIと全managed認可、世代保持/復旧・実root/boot、
残る全DEB効果、完全置換ISO、全言語翻訳等の全体要件も未完。時刻を符号化できることを実FSの復元保証にしない。

以下は完了済みの前工程である。

2026-09-10 UTC。既存NIAROOT1の原本/所有権検査へlive設定選択を接続し、最終path順の配置を作る
Pkg_Root_Configurationを追加した。root/transaction/context、incoming原本と全incoming宣言の選択網羅を検査する。
保持/更新/退避は完全な属性参照、削除はentry除外として扱う。退避と元payload/他設定の重複、
親欠落/非directory、変更対象へのhardlink依存を拒否する。最後に全選択を再確認する。
元rootのbinding、各entryの選択/閉包、fileを残さないものも含む全選択参照を保持する。

Debian 13の対象2 main強制compile、最終の配置136 assertionと既存選択270 assertionが成功した。
実原本からcatalog/保持閉包/root tarを作り、実private設定の保持/更新/削除/復元と各拒否を確認した。
24 DEB fixtureの再現性、383 compile入力と25 fixture入力の同一性を確認した。
初回3回のcompile失敗を修正し、途中133/270成功と最終136/270を区別して保存した。
構造/link/lint/licenseと生成CIも成功。Ada mainは82、数学的入力/共有vendorは不変。
全suite/証明/旧カオス/VMは反復していない。全job終了済み。

subjectはf28773a5a30a4129de0bd7746e6aff68397ef40f3e8bb18e3d45af604a0ce17e。
判断ADR-0100、証跡distribution/evidence/native-transition/root-configuration-01/、
私有lab native-root-configuration-01、最終test-05.log。3 GiB/swap0/CPU1/pids128、強制-fを維持した。
GitHub公開は未実施。

次はこの配置からの設定済みtar生成と全属性の実適用である。配置の検査を実root更新の完成とみなさない。
全過去設定の列挙、inode/link効果、ACL/capability/chown/chmodとflags/時刻の適用、特権observer、
認証UIと全managed認可、世代保持/復旧・実root/boot、残る全DEB効果、完全置換ISO、全言語翻訳等も未完。
配置読出しは準備時のsnapshotであり、実行前の再確認を省略しない。

以下は完了済みの前工程である。

2026-09-10 UTC。設定内容の選択へ対象/退避の全属性参照と数値permissionの採用元を追加した。
localは完全NIACOBS1、vendorは元DEBと元pathを保持し、現在のregularがあればvendor内容/退避も
localの全permission bit・UID/GIDを継承する。初回導入は元payloadの数値を使う。
NIACCH02に保存し、Read_Effectsは全参照とlive namespaceを再確認してから返す。失敗時は両entryを消す。

Debian 13の対象main強制compileと270 assertionが成功した。双方の退避、mode 0600/06740、
数値owner、初回/欠落、保存byte列、選択後のmode変更/退避先作成/別閉包を確認した。
初回testはfixtureのmode/owner期待値を誤認して失敗し、実原本の0640/1001/1002へ期待値を修正した。
runtime変更による取り繕いはしていない。失敗logと原本確認記録も保持した。
380 compile入力と22 fixture入力を照合、構造/link/lint/licenseと生成CIも成功。Ada mainは81。
数学的入力/共有vendorは不変で、全suite/証明/旧カオス/VMは反復していない。全job終了済み。

subjectは097b5508227fd5dc012cc68d526bee88fe2873a38184bb1e1c47c7653e3bfba8。
判断ADR-0099、証跡distribution/evidence/native-transition/conffile-attributes-01/、
私有lab native-conffile-attributes-01、最終test-02.log。3 GiB/swap0/CPU1/pids128、強制-fを維持した。
GitHub公開は未実施。

次は残る属性適用方針と全namespace/link/root archiveへの反映である。
元record参照を保つことはACL/capability/chown/chmod、flagsや時刻の適用完了ではない。
特権observer、認証UIと全managed認可、世代保持/復旧・実root/boot、残る全DEB効果、
完全置換ISO、全言語翻訳等も未完。観測値と復元可能な値を区別する。

以下は完了済みの前工程である。

2026-09-10 UTC。NIACOBS1の検査付きAda readerを追加し、実snapshot保存側からも読戻しを行うようにした。
元のraw path、namespace、全mode/UID/GID/link数、signed時刻、statx値/mask、flags、可視xattr/ACLを保持する。
metadataと内容objectのhash/サイズ、component/欠落位置、順序・長さを検査し、欠損をhostから再生成しない。
live C handleを閉じた後も読めるが、過去記録の読戻しは現在のroot/属性の真正性や復元許可ではない。

Debian 13の対象2 main強制compile、属性読戻し69 assertionと既存選択154 assertionが成功した。
実POSIX ACL/空・バイナリxattr/負・小数時刻、破損のCorrupt、期限のStale、全幅値と欠損拒否を確認した。
追加testのByte演算可視性を修正し、途中ログも保持した。380 compile入力と22 fixture入力を照合した。
source構造/link/lint/licenseと生成CIも成功、Ada mainは81。数学的入力/共有vendorは不変で、
全suite/証明/旧カオス/VMは反復していない。全job終了済み。

保持済みdpkg 1.22.22 sourceのconfigure.c/file.cから、更新内容に既存owner/permissionをコピーする処理を
確認した。上流コードは変更/取込みしていない。内容と属性の採用元を別に計画する必要がある。
原本/member hashはupstream-source.jsonへ記録。新しいreaderはその適用方針や全root更新を実装していない。

subjectは0ba58e153141ae24583f7c8b2f7e2105fc07a82349c65134f2c4f3dc94c8e64b。
判断ADR-0098、証跡distribution/evidence/native-transition/conffile-observation-01/、
私有lab native-conffile-observation-01、最終test-04.log。3 GiB/swap0/CPU1/pids128、強制-fを維持した。
GitHub公開は未実施。

次は全属性の採用方針と全namespace/root archiveへの反映である。
特権属性observer、認証UIと全managed認可、世代保持/復旧・実root/boot、残る全DEB効果、
完全置換ISO、全言語翻訳等も未完。inode/link関係・ctime/birthtime・filesystem固有flagを
そのまま復元可能として扱わず、観測/適用値を明示的に区別する。

以下は完了済みの前工程である。

2026-09-10 UTC。元DEB・実snapshotから候補を固定し、内容選択と退避/保持一覧を結ぶ内部SDKを追加した。
root/transaction/context・初期期限を候補へ束縛し、選択はその候補へ一回だけ受ける。
必須確認未解決、別候補、途中編集、退避名衝突/後発作成を拒否する。
両原本・元宣言・内容/属性参照・観測metadataと選択を既存CASの正規保持一覧へ保存する。
keep-localでも次vendor原本はincomingへ進め、通常削除/purge/宣言付き削除/省略を区別する。
通常payloadへの転換やlinkは別効果を要求する。公開コマンド・共有API/vendorは不変。

Debian 13の強制compileと私有root/CASの154 assertion、21原本fixtureの再現性が成功した。
選択/次vendor原本/保持一覧と、別候補/閉包、編集、退避先、期限、保持原本欠損と非再生成を確認した。
初回test Byte visibilityと相対media指定を修正し、途中ログも残した。
固定SOURCE_DATE_EPOCH=1788739200の再利用cacheでは更新がup-to-date扱いになったため、
最終test-06.logは対象mainをgprbuild -fで再compileした。旧152を最終154の根拠にしない。
この固定環境でcacheを再利用する今後の変更試験も対象mainを強制compileしてsourceを照合する。

377 compile入力と22 fixture入力を照合した。source構造/link/lint/licenseと生成CIが成功、Ada mainは80。
数学的入力は不変で、全suite/証明/旧カオス/VMは反復していない。全job終了済み。
subjectはada07d0d7094d368868fb7a829276f8bab6e8e5559306f49fb8066a05257d4b0。
判断ADR-0097、証跡distribution/evidence/native-transition/conffile-choice-01/、私有lab native-conffile-choice-01。
3 GiB/swap0/CPU1/pids128を維持した。GitHub公開は未実施。

次はこの内容選択を、全属性/全namespaceの計画と実root archiveへ接続する工程である。
認証UI、稼働root/intent/所有権の全managed認可、特権属性observer、独立durable reader/recovery、
世代全体の保持とpin/GC、実root/boot公開は未完。session内の選択束縛を署名付き利用者同意にしない。
site鍵/floor/時刻/installer、残る全DEB効果、完全置換ISO、全言語翻訳等の全体要件も継続する。

以下は完了済みの前工程である。

2026-09-10 UTC。実設定のsnapshotを内部C/Ada SDKとして追加した。
指定root FDからraw pathを読み、実内容と版付きmetadataを同じCAS予約で保存・再照合する。
真の欠落と不明/未対応を区別し、失敗時のCurrentはOther、metadata hashはzeroになる。
inode/namespace、mode/UID/GID/link数、可視xattr/ACL、flags、負/小数時刻を保持する。
O_NOATIMEを要求し、読取権限不足をMissingにしない。共有API/vendor・公開コマンドは不変。

Debian 13の強制compileとCAS連携41 assertion、ASan/UBSan付きC検査が成功した。
内容・inode置換・削除・祖先作成・mode/xattr/実POSIX ACL/link数・raw名・時刻・権限不足・
期限、空fileと複数chunkを確認した。ACL後に同じmodeを設定して変更を期待したfixtureを修正し、
失敗ログを保存した。最後にopen失敗のerrno保持を修正し、最終sourceで再compile/両検査を通した。
374 compile入力と3 C入力を照合。source構造/link/lint/licenseと生成CIも成功、Ada mainは79。
数学的入力は不変で、全suite/証明/旧カオス/VMは反復していない。全job終了済み。

subjectはd639aed02b6583e79580f3a10e43094af0fd05b1088ac4b5333bc8ac6597a913。
判断ADR-0096、証跡distribution/evidence/native-transition/conffile-snapshot-01/、
私有lab native-conffile-snapshot-01、最終実行test-03.log。3 GiB/swap0/CPU1/pids128を維持した。
GitHub公開は未実施。新SDKをcontrollerへ接続した、本番属性を完全観測したという意味ではない。

次は利用者選択/退避名と保持閉包、snapshotと原本属性を全root組立てへ接続する工程である。
一般userから隠れた属性とroot所有private設定には特権observerも必要である。
観測は楽観的な再照合でfilesystem凍結ではなく、同じStoreの存続とroot/世代のcontroller束縛が前提。
全managed認可、site鍵/floor/時刻/installer、全DEB効果、実boot/復旧、完全置換ISO、全言語翻訳も未完。

以下は完了済みの前工程である。

2026-09-10 UTC。元DEBのconffiles宣言と設定内容の三者比較を実装した。
旧vendor/local/新vendorを区別し、編集・削除の保持、確認要求、退避、通常削除/purge/remove-on-upgradeを扱う。
宣言hashと元payload全属性を保持し、空/不在/未知を同一視しない。raw filenameはbyte列のまま保持する。
同じASCII型制約を持っていた供給plannerのpathも修正し、共有API/vendorは不変である。

Debian 13のcompile、原本宣言/拒否99 assertion、planner UTF-8を含む26 assertionが成功した。
scriptなし・非root・私有root/DBでdpkg 1.22.22を実行し、最終126 caseの内容、確認、退避、baselineが一致した。
初回ASCII path不一致と、metadata比較で見つけたremove flagの履歴保持/省略かつlocal欠落時の追跡解除を修正した。
旧比較の成功をmetadata全比較へ読み替えず、途中の三不一致も保存した。
供給plannerの実service VM17 caseも成功。計画二要求各52 assertion、trust変更/欠損各46 assertion、
通信中のCAS競合排除32回を確認した。全VM/job終了済み。

subjectは809073d3409ae92de9c31b3e5b03260065c32d572e00be97a8c82b8324576926。
369 compile入力、19 conffile fixture、65 VM source、79 VM入力を照合した。service配布入力22は不変。
source構成/link/lint/licenseも成功し、Ada main登録は78。数学的入力・全suite・旧カオスは反復していない。
判断ADR-0095、証跡distribution/evidence/native-transition/conffiles-01/、私有lab native-conffiles-01。
資源上限は3 GiB/swap0/CPU1/pids128、VM2 GiB/1vCPU。GitHub公開は未実施。

次は実local inode/全属性の予約下観測、利用者選択/退避名と保持履歴、全root組立てへの設定反映である。
新しい判断は内容と退避義務で、全managed認可や実適用ではない。リンク/複数所有者/生成scriptも未完。
実controller/公開コマンド、site設定/鍵/floor/時刻/installer、全DEB効果、容量/再検証/回収、
実boot切替/復旧、完全置換ISO、全言語翻訳も未完。上流dpkgは隔離比較にだけ使用し製品backendへ戻さない。

以下は完了済みの前工程である。

2026-09-10 UTC。独立site trustから実observerと供給計画を結ぶPkg_Supply_Plannerを実装した。
計画専用sessionは架空のplan/map/policyを持たず、現在のroot保護policy/floorをpinする。
各原本認証とmap/保持policy作成の前後で同じtrustを再観測し、同じCAS予約を保持する。
Bind_Publicationは実際のhashへ一方向に束縛し、元のpin/時計高水位/期限を維持する。
計画用sessionの公開利用、設定の途中採用、失敗出力の残留を拒否する。

Debian 13でAda/C compile、既存observer25/site248 assertionが成功した。
実配布serviceのVM17 caseも成功。供給計画の正常二要求は各54 assertion、HTTPS中の
policy/floor更新とfloor欠損は各48 assertionで三出力消去/session停止を確認した。
既存原本認証二要求は各50 assertion。通信中のCAS競合排除は合計32回観測した。
全VM/job終了済み。source構成/link/lint/licenseも成功した。

subjectは08049713239be371a3f3da7e4a01feb043aa1e78f3af3686a69a7839ce62542c。
364 compile入力、65 VM source、79 VM入力を照合した。serviceの22配布入力は不変で、
前工程のDEB 3d393d248edf558e4b6344e2dddc8db280d4cdd308a05a519396ea128bd32c6bを再利用した。
数学的入力は不変で証明/全suite/旧カオスは反復していない。新SDKを公開controllerへ配布したという意味ではない。
判断ADR-0094、証跡distribution/evidence/native-transition/supply-planner-01/、私有lab native-supply-planner-01。
外側3 GiB/swap0/CPU1/pids128、VM2 GiB/1vCPUを維持した。GitHub公開は未実施。

次は実controllerのmanaged認可adapterと公開管理コマンドへの接続である。
plannerのpredecessorと公開束縛はcaller contextであり、実root.stateのadmissionや世代公開を代替しない。
本番site設定/鍵更新/失効、独立floor/時刻とinstaller配備、全DEB効果、容量/再検証/回収、
実boot切替/復旧、完全置換ISO、全言語翻訳も未完。VMのCA/TUF/key/root contextは人工fixtureである。

以下は完了済みの前工程である。

2026-09-10 UTC。native coreの保持原本から独立供給observerを呼び、同じCAS予約で結果を保存する
内部SDKを追加した。実sender/sealed FD/hash、独立署名と五原本、現在時刻を検査し、拒否時の二出力を消す。
公開CLI、共有API/vendor、永続形式は不変。予約を開き直さず、原本のread FDだけを渡す。

Debian 13でAda/Cをcompileし、境界25 assertion、UTF-8/JSON処理のASan/UBSan検査が成功した。
実配布observerのVM13 caseが成功。正常二要求は各50 assertionで、実HTTPS/TUF/OpenPGP/credentialから
native CAS、catalog/closure、供給mapと保持policyまでを同じStoreで検証した。
HTTPS取得中に別writerの競合排除を20回観測し、別control/UID、state/config/key/TLSと原本不一致を拒否した。
初回のAda visibilityとVM helper importを修正し、失敗ログも保持した。全VM/jobは終了済み。

subjectはe14684a7a7a689fb3071ed2e0bd8ef55e26a9cf554e4aa4ec22213d041320917。
362 compile入力、65 VM source、79 VM入力を照合した。既存serviceの22配布入力は不変で、
主DEB 3d393d248edf558e4b6344e2dddc8db280d4cdd308a05a519396ea128bd32c6bを再使用した。
新SDKの配布app/controller接続や再現性build完了を意味しない。source構成/link/lint/licenseも成功した。
不変の数学的入力・全suite・旧カオスは再実行していない。判断ADR-0093、
証跡distribution/evidence/native-transition/native-core-observer-01/、私有lab native-core-observer-01。
外側3 GiB/swap0/CPU1/pids128とVM2 GiB/1vCPUを維持した。GitHub公開は未実施。

次はこのSDKと現在site供給providerを実controllerの供給計画・全managed認可へ接続する。
本番site設定/鍵更新/失効、独立floor/時刻とinstaller配備、全DEB効果、容量/再検証/回収、
実boot切替/復旧、完全置換ISO、全言語翻訳は未完。fixtureの供給mapを実rootのadmissionや世代公開にしない。

以下は完了済みの前工程である。

2026-09-10 UTC。独立供給observerを実サービス/内部client/DEBへ接続した。
専用nia-supply UIDがnia-pkg peerの三原本FDを私有copyし、保護設定、既存TUF cache、標準HTTPS、
OpenPGPとcredential署名を使う。sealed read-only FDのreceipt/policyを返し、clientは実sender、
hash/署名/scope/時刻を検査する。公開管理コマンド、共有API/vendor、導入済みDBは変更しない。

明示provisioningだけが初期stateを作る。通常serviceはStateDirectoryを使わず、既存stateの所有/modeと
bootstrap履歴を要求する。package導入時は停止し、既定pin/seed/cacheや欠損lockを作らない。
単体9試験と実DEBのVM11 caseが成功。二つの連続要求が実HTTPS/TUF/OpenPGP、systemd credential、
実native CASの各31 assertionを通過した。state所有/権限、root peer、原本/config/key/TLS不一致、
lock欠損を拒否し、元inodeと不正state属性の非自動修復を確認した。全VM/jobは停止済み。

niaos-archive-observer 0.1.0 allのDEBと対応source tar/.dscが別directoryで一致した。
主DEB hashは3d393d248edf558e4b6344e2dddc8db280d4cdd308a05a519396ea128bd32c6b。
source subjectは036f81116950a4937a69e969152faae3043ecfbb159868533c036cff045dc38b。
22 package入力、65 Python VM入力、全79 VM入力を照合した。Ada実装は不変で既存driverを使用し、
全suite/証明/旧カオスは繰り返していない。source構成/link/lint/licenseも成功した。
証跡はdistribution/evidence/native-transition/archive-observer-01/、判断ADR-0092。
私有labはnative-archive-observer-01。GitHub公開は未実施。

次は実native coreの保持原本をこのobserverへ渡し、返されたreceipt/policyを同じCAS予約と
供給計画へ保存・検証する接続である。本番site設定・鍵更新/失効・floor/時刻とinstaller組込み、
全managed/世代認可、全DEB効果、容量/再検証/回収、実boot切替/復旧、完全置換ISO、全言語翻訳も未完。
実HTTPS/署名を使ったVMの人工root/key/DEBを、本番siteの認定や実行認可にしない。

以下は完了済みの前工程である。

2026-09-10 UTC。認証済み供給recordのcredential署名providerを実装した。
既存TUF/OpenPGP認証後だけFDから鍵を読み、独立scope/key/epoch/lifetimeを照合する。
read-only credentialまたはsealed memfd、所有/mode/正確なservice ACL、非dumpable/core禁止を使い、
既存の署名・保持policy・時刻の最終検査を維持する。任意message署名や本番既定鍵は作らない。

最終Python10+既存receipt13試験、host/VMの実認証からnative CASへの五bridge判定が成功した。
正常native31 assertion、実systemd LoadCredentialのroot所有ACL/read-only mountと、
別鍵・短いcredential・欠損の三拒否を確認した。初回のumask、ACL想定、oneshotログ取得/後始末の
不一致を修正し、失敗ログも保存した。service保護とPC負荷制限を維持し、全VM/job停止済み。

subjectは16a437d7542d96cb88da48788bde060b9c4c20d8a45a4601efd52b6fb343eeee。
358 compile入力、61 Python sourceと74 VM入力を照合した。Ada実装/共有API/vendorは不変で、
不変の全suite/証明/旧カオスを繰り返していない。source構成/link/lint/licenseも成功した。
証跡はdistribution/evidence/native-transition/archive-credential-01/、判断ADR-0091。
私有labはnative-archive-credential-01。GitHub公開はまだ行っていない。

次は本番observerの独立設定とjob/service packaging、既存TUF cacheの配備、実HTTPSとの統合、
鍵更新/失効、publisher/controllerと全managed/世代認可adapterへの接続である。
今回の一時鍵とTUF transportはfixtureで、APIの成功を本番serviceの配備完了にしない。
site floor/時計、全DEB効果、容量/再検証/回収、実boot切替/復旧、完全置換ISOと全言語翻訳も未完。

以下は完了済みの前工程である。

2026-09-10 UTC。独立した現在site供給providerを実publisherへ接続した。
Pkg_Site_Supplyがroot所有policyと独立floorから現在のscope/key/epoch/ageとOSのUTCを読む。
全祖先保護、完全hash、root/serial/時刻、contextを確認し、変更・欠損時は出力を消してsessionを停止する。
CASを開き直さず、既存公開側の予約/原本照合/全managed guardは維持する。
内部read-only配備確認appを追加し、共有API/vendorや世代/供給recordの形式は変えない。

Debian 13のcompile、248境界assertion、既存公開2023 assertionが成功。登録Ada mainは76、
app在庫は20になったが、今回全体を実行したという意味ではない。
clean pkgcore commit9de3fe6542f9cf497434855de17af602f998165eから全6 appをDEBへbuildし、
別directoryの主DEB/dbgsymが一致した。主DEB hashは
b1b850ecd20ecb411aaf98f7eb3708083855649578ccd463009d33e6a88f5d3c。
DEB buildはnocheckと関連試験を分けて記録し、不変の全suite/証明/旧カオスを繰り返していない。

使い捨てVMの実配布物とUID987で20 probe case、policy/floor変更・欠損の三session拒否が成功。
実publisherの正常109 assertionではproviderを16回呼び、鍵/epoch不一致の各79 assertionでは
公開を拒否して初期世代を維持した。他のmanaged/health/effect/署名はfixtureであり本番認可ではない。
最終362 compile sourceとVM15入力は一致。subjectは4e9865f5ff59e92bf042d26ce22215f15c02190ca8c3abeebef43f410e0c55fe。
証跡はdistribution/evidence/native-transition/site-supply-01/、判断ADR-0090。
外側3 GiB/swap0/CPU1/pids128、VM2 GiB/1 vCPUを維持し、全VM/job終了済み。
私有labはnative-site-supply-01。GitHub公開はまだ行っていない。

次は認証済み供給recordのobserver/署名providerの実配備と全managed/世代認可adapterである。
policy/floorのinstaller配備、世代rollbackからの分離、正しい時刻、全DEB効果、容量/再検証/回収、
実boot切替/復旧、完全置換ISOと全言語翻訳は未完。root所有とhashをhardware rollback耐性にしない。

以下は完了済みの前工程である。

2026-09-10 UTC。内部native storage bootstrapを配布物へ接続した。
新しいpkg_store_bootstrapは非rootで正規MC_Store.Initialize/Openを呼ぶ。
root側は固定path/policy/停止unitを検査し、排他的intentを永続化してからCAS/保護bankを作り、
完了を別記録へ束縛する。途中・既存状態の上書きや通常起動からの自動初期化をしない。
独立認可が未配備なのでbootstrap成功ではsocketを有効化しない。共有API/vendorは不変。

Debian 13の実compile、配布ELFの18場合、通常root archiveの201 assertion、実VMの207 assertionが成功。
二つの配布物それぞれ主DEB/dbgsymの別directory再現性を確認した。
pkgcore主DEBは82c26c92b235a57a1b2aa8fddc506a914a24fcdff8d49e2997f9daebf45ee175、
root準備0.2.0主DEBはa86a0ffd44854f33a455d16db51588cb30e501327aed05ba00a83cf7934f0667。
実bootstrap後にfixture driverが既存CASを開き、以前のSIGSTOPによる調整を廃止した。
七つの初期化拒否、再起動後の履歴、欠損拒否、初期記録/lockのinode保持と元入力hashを照合した。

初回のbuild依存不足とKVM user権限の起動前失敗も保存した。ホスト権限を変えず既存一般userでVMを実行した。
外側3 GiB/swap0/CPU1/pids128、VM2 GiB/1 vCPUを維持し、全job終了済み。
全suite・不変の形式証明・旧カオスは再実行していない。pkgcoreのDEBはnocheckで関連試験と分けて記録した。
四つのREADMEに残った旧MIT説明も訂正し、現行READMEのlicense検査を追加した。

最終subjectはd0386ba03efcdc61a7055f40488ccbe565e647190345e1509f9e8a9f3ff5443c。初回全受入後の差はVM試験工具だけである。
追加の永続記録照合は受入diskの新規差分から実行し、報告field名も意味を明確にした。
製品19入力とcompile/test source358個は全一致。証跡は
distribution/evidence/native-transition/storage-bootstrap-01/、判断はADR-0089。
私有labはnative-storage-bootstrap-01、全VMは停止済み。

次は独立した供給/世代認可providerと製品controllerへの接続である。
導入先選択/保守環境、全DEB効果、容量/物理再検証/回収、実boot切替/復旧、完全置換ISO、
全言語翻訳は未完。GitHub作成/Release利用は利用者が許可済みだが、まだ公開していない。

以下は完了済みの前工程である。

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
