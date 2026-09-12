# Nia OS 開発・配布検証状況

2026-09-12 非同期native管理者認証を実装（ADR-0125 / REQ-162）。
既存polkit SDKを専用root子のpkg_operator_guardで動かし、root-preparation 0.11.0の親側APIが
peer/子pidfdとpipeを非blockingで監視する。確認番号、元期限、返答の時刻/鮮度を固定し、
古い初回返答、取消、子停止、失効後の再利用を拒否する。保存grantや自動再認証は追加しない。
最終実DEBで11 polkitケース、3単体/有限制御検査、strict typing、対応ソース照合が成功。
最初のVM試験は再起動過多でstart-limit-hitになり、harnessの不要な再起動を削減して解決した。
その後の鮮度修正ではcontrollerだけ再buildし、同一pkgcore DEBを最終受入に再利用した。
証跡はdistribution/evidence/native-transition/operator-guard-01/。本番認証dialog/計画同意、
native世代guardと実効果遮断をつなぐ全supervisor、全Ada/Python/FFIの形式保証は未完。

2026-09-12 保持rootの再検査handoffを実装（ADR-0124 / REQ-161）。
準備用とは別の224 byte要求と応答を使い、元の展開期限、独立期待mount/inode/device、
世代と原本/worker/stage、現在交換期限を固定する。送信試行後の別操作への変更も拒否する。
実Ada/C/Pythonの32通信caseとstrict typingが成功。純粋C validatorのCBMC 288 propertyと
厳格なGCC静的解析も成功した。証跡はdistribution/evidence/native-transition/root-reinspection-handoff-01/。
これは通信SDKの受入であり、実物理再検査、本番supervisor/認可/計画同意への接続、全C/FFIの
形式保証は未完。実DEB/ISOと不変componentの全体suiteは再実行していない。

2026-09-12 独立供給方針の初回配備を実装（ADR-0123 / REQ-160）。
root-preparation 0.10.0は管理者が独立に用意したpolicy/floorを既存native readerで検査し、
耐久記録と上書き禁止で公開する。pkgcoreの--planningは架空の公開plan/mapを要求しない。
正常、不一致、期限切れ、公開3境界のSIGKILLを最終実DEBで受入した。再試行拒否と非root拒否も成功。
floor公開後・応答前の停止では有効な組が既に見える場合を確認し、完了不確定として扱う。
6単体/有限制御検査、strict typing、構造/lint/license、原本→対応ソース→実DEB照合が成功。
証跡はdistribution/evidence/native-transition/supply-initialization-01/。形式検査は有限制御のみ。
本番鍵の由来・非rollback anchor・方針更新/復旧、認可/計画同意と世代管理への全体接続は未完。
全体suite/不変C・SPARK証明は反復せず、独立再現build・実電断・本番OS認定は今回に含めない。

2026-09-12 開発storage: 旧導入VM2台とbuilder内の/build-03〜/build-09を整理し、
実割当59,774,562,304 byteを回収した。空きは約4.1 GiBから約59.7 GiBへ回復。
最大の開発用単一file builder.qcow2は58.8 GBから18.5 GBへ減少した。元ISO・対応ソース・
工具と受入記録は維持。旧build recordはguest内の/build/retired-build-records-20260912.tar.xzへ保存。
ISO suiteは全項目成功後に導入diskだけを整理し、明示保持/失敗時は残すよう変更した。
image工具20件と実QEMU lockの削除拒否/停止後削除が成功。新ISOの全起動試験は反復していない。
証跡はdistribution/evidence/development-storage/reclaimed-01/。本番接続と出荷認定は引き続き未完。

2026-09-12 root worker実行中の取消を実装（ADR-0122 / REQ-159）。
展開/物理再検査中に依頼元socket/pidfdと元期限を監視し、取消時に専用process groupを
未回収leaderへ束縛したまま停止する。pipe容量・event予算・回収待ちを有限化した。
root-preparation 0.9.0の実DEBを一度構築し、同じ成果物を二つの専用VMで受入した。
通常のprepare/freeze/verify/observe/closeと、実native workerのSIGSTOP後接続断、
worker終了・RO化・attempt保持・再要求拒否が成功。後者の観測値は約0.076秒であり時間保証ではない。
8件の実プロセス/有限制御試験とstrict typing、構造/lint/license、配布ソース照合も成功。
証跡: distribution/evidence/native-transition/root-worker-monitor-01/。
全runtimeの形式証明、本番供給/認可/計画同意からの接続、全DEB効果・boot/復旧は未完。
不変のC/SPARKの全証明や全体試験は反復していない。0.9.0の独立再現buildもこの区切りには含めない。

2026-09-12 GitHub配布CI: run 34716536899（f1599f9）と34716711208（da62319）が成功。
後者は同じ固定Debian入力の軽量package-builderを使用し、management 0.1.1と識別0.2.0をbuildした。
submodule取得、実package配置、12入口、媒体索引/一覧、日本語表示、未接続更新の拒否、
識別情報の可逆install/reinstall/remove/purgeを確認した。全体OSの受入ではない。
証跡はdistribution/evidence/management-interface/packaged-01/ci-*.json等。
今回のjobはすべて終了。本番認可/同意・全DEB効果・実boot/復旧等は未完である。


2026-09-12 niayan公開後の配布統合: 9repoの公開mainをGitHubへpushし、初回commitをAPI照合した。
niayan-managementを追加し、採用12入口・必要な14 Python module・7翻訳catalogを明示exportする。
配布manifestは全sourceへ束縛し、旧public nia aliasをsource/main/artifactから撤去した。
管理器fingerprintと公開人工fixtureを正本工具で更新。共有契約とC/FFIは変更していない。
識別packageは0.2.0、managementは0.1.0の開発版。全DEB効果・本番認可・実起動切替は未完。
限定した配布checkpointで、実management DEB構築、固定containerへのinstall、全12入口help、
非rootの実媒体索引/一覧・日本語表示・未接続操作の拒否とpurgeが成功した。
旧aliasのない2つのcontrolcore mainも固定containerでbuild成功。全体proofの反復は行っていない。
新しいManagement and identity packages CIは変更した2 source packageだけを構築・受入する。
出荷条件全体、完全置換ISO、全言語・形式保証・実機認定はPRODUCTION.ja.mdで引き続き未完。


2026-09-12: 利用者は公開名niayanとGitHub公開を指定した。OS表示・GRUB・ISO設定・
liveユーザーをniayanへ変更し、識別パッケージ版を0.2.0へ進めた。内部DEB名と保存形式は維持する。
READMEの過去の試験数を現行全体の成功と誤読しないよう対象範囲を明記した。
公開先はminto-dane/niayanとniayan-*の8子repo。公開前のmain履歴9repoのGit整合性と
サイズを確認し、gitleaksの3,122候補はhash・trigger名・公開人工fixture鍵として分類した。
詳細はdev/initial-publication-review.json。機密の完全不在を証明する検査ではない。
変更した配布工具の既存16試験、ライセンス・構造・構文・参照確認は成功。
C/Ada/特権runtimeは変更しておらず全体compile/proofの反復は行っていない。
CIはPRと統合checkpointで起動し、独立componentの全証明は手動run_proof指定へ集約した。
新しいniayan ISOの構築・起動受入と、本番全体の完成は未実施。PRODUCTION.ja.mdの順に進める。


2026-09-10 UTC。Debian 13ベースの起動・導入可能なKDE開発版。実ISOのVM受入を完了し、既存コンポーネントの実コンパイル、実行試験、再現性、独立Git管理も整備した。本番認定・実機認定は行っていない。

## 最新依頼: Niaへの完全置換とハードニング

### 直近の検証

2026-09-12 UTC追補。旧root準備service/socket、専用C/Ada RPC、旧dev viewとVM bridgeを撤去した。
ADR-0120、REQ-158、HAZ-144/145、FAULT-157/158。SDKのPrepare_Root/Reinspect_Root_And_Holdは
必須transportへ統合し、独立observerと全認可/保持内容/現在設定/実FD/三予約を維持する。
共通Root_IdentityはPkg_Root_Identityへ分離した。旧Using/socket直結APIとfixture引数は残さない。
共有Bank、bootstrap、FrozenRoot、版付き復旧記録と必要なsource/licenseは維持した。
重複した配備試験をdevice/bootstrapと後継session試験へ統合した。

0.8.0 DEBは旧所有ファイルを除去し、制御面のlive更新をpreinstで拒否する。
オフラインchroot unpackによる旧0.7.0からの除去と記録保持、新規VMの完全なpackage導入を確認した。
旧版と後継listener稼働中の更新拒否で、unit/PID/コード/保存物は不変だった。
chrootのconfigureと処理中workerへの更新はこの受入に含めない。
main/debug DEBとDSC/source tarの独立2 buildはバイト一致。main DEBは
ba88f35d97df513ee0c3a194944f407c312038eb225ce311a48057e32067473e。

固定containerで5つの選択Ada mainをcompile/実行した。v5は1,631、v6は1,206 assertion。
設定entry 141、通常世代stage 1,211、UID0拒否1,133 assertionも成功した。
root sessionの実C/Ada/peer/FD境界は29項目成功。世代fixtureの認可/identityは人工である。
v6の呼出元の選択誤りは実run_root_configuration_testsの追加実行で訂正し、途中の準備失敗も記録した。
実VMで共通Bankのintent永続化後SIGKILL、物理再検査、欠損lock/policyの実要求拒否、
専用device bootstrap、後継sessionのprepare/freeze/observe/close、二段階の再起動後ROを確認した。
SIGKILLはworker開始前の所有processであり、全電断や本番取消の受入ではない。

全jobは終了。重い処理は3 GiB/swap0/CPU1/pids128で逐次、VMは2 GiB/1 CPU。
compile imageは76d5c00d…、QEMU工具imageは7f92f649…で、完全hashは証跡に記録した。
今回の不要VM/旧SDK/試験cacheから215,363,584 byteの割当を削除した。共有builderと無関係のVMは維持した。
subjectはdaac325557fae401f562333cb5cf1ff84c0bc5c7603736dc4d1ee5e3e4320ba8。
構造/参照/lint/license/生成CIと現行source→配布物照合が成功。証跡は
 distribution/evidence/native-transition/root-service-retirement-01/（63 file、SHA256SUMS込み）。
私有labはroot-service-retirement-01。現在のworkspace/buildとpackage/sourceは次の接続用に保持した。

本番認定/公開は行っていない。次は本番の現在供給/世代admission、正確な同意、
root handoff/保持session/独立観測と物理遮断を非root世代SDKへ接続する。
C全体/FFI/重要runtimeの形式検証と厳格規則適合、全writer排他/slot/保持/GC、
実root/boot切替・復旧、全DEB効果、完全置換ISO、全言語翻訳は未完である。
既存minto-dane/niaosは別projectなので上書きしない。

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

以下は前工程の記録であり、各subjectに対する結果として保持する。

2026-09-12 UTC追補。利用者の追加条件を、言語と影響に応じた必須の実装保証基準へ反映した。
規範はassurance/docs/engineering/specs/implementation-assurance.ja.md（ADR-0117）。
CだけでなくAda/SPARK、SPARK対象外/FFI、特権Python、UI、シェル/配布/CIを対象とする。
NASAの要求追跡・保証活動とJPLの具体的制約を参照するが、航空宇宙認証や全規格適合は宣言しない。
自作C16unit（runtime11）のinventoryを保存し、全Cの形式検証・厳格規則適合は未完と明示した。

実runtimeの純粋wire検査関数とhelperについて、CBMC 6.6.0の208条件が成功した。
任意の192byte内容とlength/deadline、NULLを検査し、正規形式との同値性とメモリ/整数操作を扱う。
反復上限不足の負の対照は期待どおり失敗。厳格警告とGCC analyzerは実compileを伴って診断なしを確認した。
工具/仮定/入力hash/未証明範囲を保存した。通信/OS/FD寿命や全Cの証明へ拡大しない。
CIへ限定証明を追加し、固定CBMC依存を7componentへ同期した。新dev imageの全buildとremote CIは未実行。
証跡はdistribution/evidence/implementation-assurance/initial-01/（17 file、SHA256SUMS込み）。

非root世代SDKに必須transport付きPrepare_Root_Usingを追加し、元の全認可/予約条件を保持した。
root親子のprivate seqpacketとpidfd/各message資格情報/実archive・CAS FDを使うhandoffを実装した。
独立scopeと元期限に束縛し、送信後不明をIndeterminateとして扱う。ADR-0118。
15項目の実kernel境界検査とsanitizer runner、3 Ada mainとv5/v6回帰が成功した。
sanitizer runner内のAda execは非instrumentedである。425個は照合したビルド入力数でありcompile件数ではない。
最終型注釈付きPythonはsanitizer runnerで検査した。厳格型検査と形式的モデル対応は未完。
初回fixtureの取消RST/ディレクトリ権限失敗も保持した。C transport全体の新基準適合は未完。
証跡はdistribution/evidence/native-transition/root-handoff-01/（38 file、SHA256SUMS込み）。

source subjectは462da7431ca1adb554a012199e26649b33bb3f3a0c785fe34590d345bbda53f6。
構造/参照/lint/license/生成CIは成功。root工具は別のroot-inputs.jsonで照合した。
全job終了、重工程3 GiB/swap0/CPU1/pids128。今回VM起動/ストレージ削除/公開は行っていない。
次は新基準へ重要runtimeを適合させつつ、独立root supervisorの現在供給/世代admission、正確な同意、
実root sessionと再観測、取消・遮断へこのhandoffを接続する。現時点では製品接続は未完。
全writer排他、bank slot/保持/GC、実root/boot切替・復旧、全DEB効果、完全置換ISO、全言語翻訳も未完。
既存minto-dane/niaosは別projectで上書きしない。GitHub公開許可は有効。本番認定は行っていない。

以下は前工程の記録であり、各subjectの検証結果として保持する。

2026-09-12 UTC追補。自作6コンポーネントのRPM定義に残っていた旧MIT License fieldをBSD-3-Clauseへ修正した。
現行LICENSING.mdと過去のMIT許諾文も同梱対象にした。dev/check-licenses.pyはRPM Licenseと自作DEB copyrightも照合する。
修正前の実6定義の拒否と修正後の成功、構造/参照/lint/生成CIを確認した。runtime/数学的入力は不変で、重い検査を反復していない。
RPM buildは未実施。第三者原本/過去証跡/既存許諾は保持した。ADR-0088追補、証跡は
 distribution/evidence/licensing/package-metadata-01/（21 file、SHA256SUMS込み）。
現在subjectは3946b76aa30756cd060789af6317816e36a75993684aa0d4d608829bebbb636a。
rootの検査器はこのsubject外なので、別のroot-input.jsonへ最終hashを記録した。
以下の認証SDK受入は固有subjectのまま保持し、配布metadata変更後に実行し直した件数にはしない。

2026-09-12 UTC。実polkitへ照合するroot supervisor専用Pkg_Operator_Authorizationを実装した。
accepted seqpacketのkernel peer pidfd/UIDと、独立のplan/requestを固定system busへ送る。
元boottime期限は最大120秒で、retained認証を拒否する。Checkはcontext/peer/取消/期限とunique owner/Changedを確認し、
失効後の再利用を拒否する。自身のFDだけを解放する。供給・正確な計画への同意・native admissionは別の必須検査である。

C/Adaと既存6アプリのcompile、選択Ada mainの独立directoryでの同一bytesを確認した。
418個のビルド入力集合を照合した。全418unitのcompile件数ではない。private busの12項目、ASan/UBSanの12項目、
実Debian polkit 126-2 VMの14項目が成功した。実pidfd、既定拒否、限定rule、実rule変更、owner再起動、
取消/peer終了/期限、実Ada/C往復を確認した。実agent/PAM dialogは未検査。fixture ruleは削除済みで製品へ同梱しない。
ASanのPython全体leak報告は無効で、address/UBは停止し、FD寿命は別に実数検査した。

0.7.0 service packageはauth_admin（keepなし）のpolicyとpolkitd依存を追加し、main/dbgsym/dsc/sourceの二重buildが一致した。
main DEBは56191f395fe77ac532dc6b7b4b7b78a31d0bc47436487fc01204d537e46d4346。
32 export入力、runtime archiveの10 file、DEB内14 module/unit/policyを正本へ照合した。
既存controller/worker/unitは不変で、今回root抽出を反復していない。C libraryは
d87a19da393a7d5eb1add90a606e6dd3fd2a501058ac940bf7b47266c4b7588d、Adaは
e62bfc563ed55e4b11813aed0332f4ff043a7f5a71465a21546874bb8accf404。
初回fixture compileと依存版指定の失敗も保持した。構造/参照/lint/license/生成CIは成功し、全suite/数学的証明は反復しない。
export後の非compile差は生成CIのmain登録とRPMのsystemd-devel依存。RPM buildは未実施。

今回の全jobは終了した。重工程3 GiB/swap0/CPU1/pids128、VM2 GiB/1CPUを維持し、終了VM差分64.01 MiBを削除した。
稼働中の別VM、base/受入VM/source/package/SDK/logは保持した。
subjectは59811cc91ab37ecdd8140045803ffefd55e4ffe93d7cb9431fca64ce433e354a。
ADR-0116、証跡distribution/evidence/native-transition/operator-authorization-01/（51 file、SHA256SUMS込み）。
私有labはnative-operator-authorization-01、受入packageはvm-package-01/packages。
GitHub公開/remote CIは未実施で許可は有効。既存minto-dane/niaosは別projectなので上書きしない。

次は独立root supervisorの現在供給/世代admission、正確な利用者同意、取消・遮断と非root世代SDKへの認証済みhandoffを接続する。
既存の必須callbackをpolkitのtrueへ置換せず、非root SDKのUID拒否を解除しない。SDKだけの成功を製品接続としない。
全writer排他、bank slot/保持/GC、実root/boot切替・復旧、全DEB効果、完全置換ISO、全言語翻訳は未完。
policyの翻訳も英語/日本語のみである。実稼働・本番認定は行っていない。

以下は前工程の記録である。

2026-09-12 UTC。root supervisor専用のnative session SDKを追加した。Pkg_Root_Sessionのlimited controlled型が
root_session.cの接続を保持し、明示scope/pin/実FDと全正規応答、root peer/message UID/PID、元期限を照合する。
Open/Observe/Close、使用中handle拒否、観測失効後の接続保持、Ada Finalizeによる切断を実装した。
既存非root世代SDKのUID/API/永続形式は不変。返却inodeを独立観測やsite認可・起動許可へ変換しない。

固定containerで選択Ada mainと必要C/Ada unitをcompileした。root peerの29項目とCのASan/UBSan 28項目が成功。
scope/identity/期限、非正規/過大/切断、余分FD/control切詰めと解放、UID/PID/fork、観測失効、Close/Finalizeを確認した。
ASanのPython全体leak報告は無効で、address/UB errorは停止する。FD寿命は別に検査した。
独立directoryの選択Ada実行物が同一bytesで、hashはb72206be3a5177b62255cd47750957db06a43de122895b6104708096483032aa。
413個のビルド入力集合を照合した。全413unitのcompile件数ではない。新mainは標準台帳/生成CIへ登録した。
構造/参照/lint/license/生成CIは成功し、Ada全suite/数学的証明は反復していない。

実GPT/ext4 VMでは受入0.6.0 package/initializerと新C libraryでprepare/observe/Closeが成功した。
実展開/RO全再検査、独立root FDのmount/device/inode/RO、新CAS OFD取得とBank保持、EOF、元tree/記録の不変を確認した。
service packageは変更・再buildせず、DEB内13module/unitを正本へ照合した。新C libraryは
7fdea19c1aaf352fa8c9d1615c6f120fa86bfdc445a2a2ca435b662ab35f4aae。Adaの実FFI往復はcontainer peerで検査した。
初回compileの異なる整数型のothers aggregateを修正した。初回入力snapshotは未保存で失敗logを診断として保持する。
thread/fork warningはpeerを別processへ変更して解消した。ADR見出しと生成CIの初期不一致も保持した。

今回の全jobは終了した。重工程3 GiB/swap0/CPU1/pids128、VM2 GiB/1CPUを維持した。
終了済みVM差分と追加diskの計47.60 MiBを削除した。稼働中の別VM、base/受入VM/source/package/SDK/logは保持した。
subjectはd7d795ce6286962f21fbfd61df1c851cc3c98fb939c705b4d103d0e14569dbbc。
ADR-0115、証跡distribution/evidence/native-transition/root-session-sdk-01/（47 file、SHA256SUMS込み）。
私有labはnative-root-session-sdk-01。SDK buildはworkspace/pkgcore/build、実0.6.0 packageは前labのvm-package-07/packages。
GitHub公開/remote CIは未実施で許可は有効。既存minto-dane/niaosは別projectなので上書きしない。

次は独立root supervisorのsite認可/供給/利用者同意・取消寿命と、非root世代SDKへの認証済みhandoff/observerを接続する。
root専用transportを非rootで呼ぶためにUID拒否を解除せず、返却inodeから独立期待値を捏造しない。
外部特権writer排他、bank slot/保持/GC、実root/boot切替・復旧、全DEB効果、完全置換ISOと全言語翻訳も未完。
人工scope/peerと実RPC接続を本番admissionや実稼働世代への接続完了とは扱わない。

以下は前工程の記録である。

2026-09-11 UTC。初回の空bankを準備するroot supervisor用controller sessionを実装した。
接続元/各messageのkernel UID0・PIDとpeer pidfdを照合し、独立request/worker/device plan/boot/bank identity、
実CAS/archive FDへ束縛する。永続O_EXCL attemptを同期してからRWへ変更し、7 capabilityへ縮小したchildで
元Bank.prepare/verifyを実行する。RO全再検査後にBank/device/rootを保持し、受信CASコピーを閉じてreadinessを返す。
observeは新CAS OFDで行い、close/切断/期限切れで自身の予約を解放する。使用済みbankをRWへ再利用しない。

実packageと専用GPT/ext4 VMで通常準備/observe/close、非root・誤worker/mount/plan/FDの拒否、
新CAS取得とBank保持、元tree/記録不変、使用済みbank拒否が成功した。再起動後ROと旧writer拒否も成功。
切断・期限切れは別VMで成功した。SIGKILL試験では同じcgroupのExecStopPostまで巻き込まれる失敗を検出し、
OnFailureによる別cgroupのseal serviceを追加した。最終VM 07では保持bankの試験用RW driftとcgroup全体のSIGKILL後に、
独立serviceがROへ戻し、元tree/記録を維持した。正常完了記録を捏造していない。
通常/切断/期限切れのcodeは最終buildと同一bytesで、新しい故障経路を最終unitで検査した。

初回prepare/inspectの追加field比較不備を修正し、実extracted結果を読取保存した。
診断globを非rootで展開した失敗とstop hook巻き添えの失敗も保持した。
最終0.6.0のmain DEB/dbgsym/source dsc/source tar.xzは二重buildで完全一致した。
31 export入力、38 runtime file、DEB内module/unitを正本へ照合した。workerは
b55000d2e21d96c8e75a9f36dda4bbcf5c77c9dbf42074fa39b1600b1c113322で不変。
実initializerは前工程の受入packageを再使用し、app/vendorの不変を照合した。構造/参照/lint/license/生成CIも成功。
Ada全suite/証明とISO buildは反復していない。

3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPU。全job終了済み。VM差分7個と追加disk7個、352.71 MiBを削除し、
base/受入VM/source/package/入力archive/既存SDKとinitializer buildは保持した。
subjectはad96a946895f429ce1a8ba518a28097c41460e02eeacfd0dabb703348baad971。
ADR-0114、証跡distribution/evidence/native-transition/root-session-01/（113 file、SHA256SUMS込み）。
私有labはnative-root-session-01。最終packageはvm-package-07/packages。GitHub公開/remote CIは未実施。
許可は有効だが既存minto-dane/niaosは別projectである。

次はnative SDK adapterと独立root supervisorのsite認可/供給/同意・取消寿命を接続し、bank slotの割当て/保持/GCを実装する。
このRPCはroot管理面を信頼し、site admissionや一般利用者consentを独立検証したものではない。
controllerはhost mount権限を持つ信頼された部品で、外部特権writer全体を封じる完全sandboxではない。
実root/boot切替・復旧、全DEB効果、完全置換ISOと全言語翻訳も未完。物理電断、RW展開の全位置でのSIGKILL、
kernel I/Oの厳密な期限、全異常でのseal成功は未認定である。

以下は前工程の記録である。

2026-09-11 UTC。明示的storage bootstrapへ専用GPT/ext4 bankの配備と起動時device照合を接続した。
root所有0600のplanでpartition UUID・filesystem UUID・容量を指定し、実block FDとcacheなしprobeへ照合する。
intent/完了記録へplan hashを束縛し、mount drop-inを新規作成・同期する。通常mountはROとし、
初期化区間だけRWで元bank provisionerを呼び、ROへ戻した現在照合後に完了記録を保存する。
準備serviceの前に独立oneshot guardが現在device/mount・plan/記録を照合する。service本体の権限を拡大しない。

配布用0.5.0のmain DEB/dbgsym/source dsc/source tar.xzは二重buildで完全一致した。
最終VMでは実native initializerによる初期化、plan欠損/UUID/容量違いと既存状態の7拒否、再初期化拒否が成功。
実再起動後の同じbank記録のinode/hash、RO mount、guard経由のservice開始、plan変更による開始拒否、
lock欠損の非再生成と明示復元後の照合も成功した。mount IDは69から67へ変わり現在値を再観測した。
初回のguard unit梱包漏れをinstall manifestで修正し、失敗入力とログも保持した。
26 export入力とsource package、30 runtime file、DEB内module/unit/workerを照合した。
workerはb55000d2e21d96c8e75a9f36dda4bbcf5c77c9dbf42074fa39b1600b1c113322で不変。
実initializerは以前の受入package 0.1.0+gita3640276f48dを再使用し、app/vendorの不変を確認した。
構造/参照/lint/license/生成CIも成功。全componentの最新buildや旧service fixture全体/証明の反復はしていない。

3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPU。全job終了済み。VM差分2個と追加disk2個、99.03 MiBを削除し、
base/受入VM/対応source/package/既存SDKとinitializer buildは保持する。
subjectは746a5a7d63171fb0666b3b9741596fc529ef7b8ebd39656ebe07c73e27311288。
ADR-0113、証跡distribution/evidence/native-transition/bank-device-01/（51 file、SHA256SUMS込み）。
私有labはnative-bank-device-01。GitHub公開/remote CIは未実施で許可は有効。既存minto-dane/niaosは別projectである。

次は本番controllerの認証/RPC・全寿命のmount/device排他とbank slot管理を接続する。
完全置換ISOのpartition recipe/UI、効果直前の現在性検査、実root/boot切替・復旧も必要である。
UUIDは暗号学的認証ではなく、clone/hotplugや特権raw writerを単独防御しない。旧bind bank/旧完了記録は
自動移行せず拒否する。LUKS/device-mapper/RAID等の別profile、全DEB効果、GC、全言語翻訳も未完である。

以下は前工程の記録である。

2026-09-11 UTC。専用ext4 bankのfilesystem単位の書込排他を内部controller部品へ実装した。
FrozenRootは独立期待mount/device/inode・元intent/worker・実CAS予約を照合し、共有subtree/子mountを
拒否する。MS_BINDなしのread-only remountで全mount viewの通常writerをkernelに排除させる。
bank.lockはO_RDONLYによる排他flockへ変更した。Close/失敗で暗黙thawせず、現在の標準bind bankや
既存serviceのcapability/RPCを自動変更しない。専用bankを製品へ配備するinstallerは未完である。

配布用内部部品0.4.0のmain DEB/dbgsym/source dsc/source tar.xzは二重buildで完全一致した。
実DEB導入・module bytes・unitを確認し、socketはdisabled/inactiveを維持した。
VMでは誤identity/subtree/子mount、書込FD/mmap、別mountのwriter、read-only Bank再起動/排他、
Close後の非thawと特権remount後の拒否が成功した。Bankのpeer/FD/worker/service中断回帰も成功。
実kernel排他/観測を使ったSDK結合は設定済み世代482・通常世代937 assertionが成功した。
件数には時刻待ちを含む。5拒否条件、成功/期限切れの三予約保持、使用中handle拒否、Closeと元root/記録の不変を確認した。

初回mmapが検査対象rootのatimeを変えた不一致を記録し、probeをrootの外へ分離した。検査は弱めていない。
SDK結合の初期VMは最初の要求前にtimeoutとなり、live診断でext4 fsync/journal待ちを観測した。
以前の受入と同じguest RAM上のloop backingで最終試験が成功した。永続ディスク性能/物理電断は未認定である。
24 export入力とsource package、83 runtime file、401不変SDK入力・32 fixtureを照合した。
workerはb55000d2e21d96c8e75a9f36dda4bbcf5c77c9dbf42074fa39b1600b1c113322で不変。
構造/参照/lint/license/生成CIも成功し、Ada全suite/数学的証明は反復していない。

3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPU。全job終了済み。共有使い捨てVM差分1個511.33 MiBを
削除し、base/受入VM/対応source/package/前工程の最終SDK buildは保持した。
subjectはdf59c0171fd025fea8a5e4437847edb94a2361cbb63bbc880f69862a70c5a210。
ADR-0112、証跡distribution/evidence/native-transition/bank-freeze-01/（78 file、SHA256SUMS込み）。
私有labはnative-bank-freeze-01。GitHub公開/remote CIは未実施。許可は有効だが既存minto-dane/niaosは別projectである。

次は専用bankのinstaller配備と永続device identity、本番controllerの認証/RPC・全寿命のmount/device排他を接続する。
効果直前の現在性検査、実root/boot切替と段階別復旧も必要である。fixture bridgeを本番配備せず、
read-only観測だけを起動許可にしない。本番source/consent/supply provider、全DEB効果、GC、完全置換ISOと全言語翻訳も未完。

以下は前工程の記録である。

2026-09-11 UTC。実rootの再検査をnative SDKと予約保持へ接続した。
元展開期限からintent hashを再構成し、新しい期限と独立期待mount/device/inode・worker・archiveを
canonical応答全体へ照合する。新generic Reinspect_Root_And_Holdは独立Observe_Rootを必須とする。
世代/root/CAS予約下で保持内容・現在設定元・認可を前後確認し、専用limited型に三予約とarchive FDを保持する。
期限切れで観測を無効にしても予約は明示Closeまで維持する。使用中handleの再要求はConflictで置換しない。

固定SDKで3 mainを強制compileした。実0.3.0サービス/workerを使ったVMでは設定済み世代477、
通常世代933 assertionが成功した。各世代の観測拒否・誤mount/元期限・応答後観測変更/認可拒否、
実treeと記録の不変、成功/期限切れでの三予約保持、使用中再要求拒否と明示Closeを確認した。
旧世代処理1,211 assertionも成功した。時刻待ちassertionを含む件数は実行依存である。
VM 01の応答/FD後片付け競合は失敗ログを保持し、新SDKが同じ期限でpeer終了まで待つよう修正した。
VM 02では応答後のFD後片付けを100 ms遅らせて確認した。通信異常/期限切れ時の全FD解放を保証してはいない。
旧展開Requestとサービス/workerのbytesは維持した。workerはb55000d2e21d96c8e75a9f36dda4bbcf5c77c9dbf42074fa39b1600b1c113322。

401 compile入力、32 fixture、4 VM工具と梱包driver/工具/DEBを照合し、構造/参照/lint/license/生成CIも成功した。
七つの数学的src/共通vendorは不変。全suite/証明/SDK binary二重buildは反復していない。
3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPUで順次実行した。全job終了済み。
今回の使い捨てVM差分2個、57.14 MiBを削除した。base/受入VM/source/現行SDK buildは保持する。
subjectは37634928f5bc298f03d256e58849c9204804ba2974a5cdcef00745ba994cb058。
ADR-0111、証跡distribution/evidence/native-transition/root-reinspection-sdk-01/（53 file、SHA256SUMS込み）。
私有labはnative-root-reinspection-sdk-01。GitHub公開/remote CIは未実施で、実施許可は引き続き有効。
既存minto-dane/niaosは別projectなので上書きしない。

次は本番の独立controllerがbank/全writer/mountを予約し、handleのClose後まで維持するproviderを接続する。
Heldだけでprovider取消やmount変更を認定しない。効果直前の現在性検査と実root/boot切替・段階別復旧が必要である。
この型を論理公開や起動許可へ流用せず、fixture bridgeを本番配備しない。本番source/consent/supply provider、
世代GC、全DEB効果、完全置換ISOと全言語翻訳も未完である。

以下は前工程の記録である。

2026-09-11 UTC。展開済み実rootの非更新再検査を内部workerとBankサービスへ接続した。
独立read-only/nodev/nosuid/noexec mountとbank/CAS予約を要求し、元intent・現在worker hashを照合する。
保持tarを二回hashし、内容/owner/mode/宣言時刻/ACL/宣言flags/link/deviceに加え、xattr集合、
全directoryのentry、正規path、子mountとinode hardlink groupを検査する。成功観測は実mount IDと
device/inodeへ束縛し、応答後も現在path・予約・元記録・期限を確認する。元rootとintent/resultは更新しない。

配布用内部サービス0.3.0のmain DEB・dbgsym・source .dsc/.tar.xzは別directoryの二重buildで完全一致した。
実DEBを導入した使い捨てVMで正常と8種類の不一致、書込可能root/異なるgenerationの拒否、Bank再起動、
実UID1000の二FD RPCが成功した。treeの内容・時刻を含む属性と元記録の前後一致、lease維持を確認した。
従来の実展開・Bank peer/FD/worker/service中断も成功した。導入unitを検査し、socketは無効・非稼働を維持した。
最終workerはb55000d2e21d96c8e75a9f36dda4bbcf5c77c9dbf42074fa39b1600b1c113322。
23 export入力とsource package、4 VM工具入力、DEB内service/workerを正本・実結果へ照合した。
構造/参照/lint/license/生成CI整合性も成功。Ada/数学的入力は不変で全suite/証明を反復していない。

初回KVM権限拒否、旧時刻の二重build差分、guest /tmp消失による診断失敗も保持した。
初回のpackage差分原因は確定していない。未来だったchangelog時刻を訂正し、新規exportと永続guest directoryで
最終build/VMを通過した。古いmanifestは流用していない。初期VMのworkerと最終DEBのworkerは区別する。
CI recipeへworker compileと依存を追加した。更新後native test imageの構築とremote CIは未実行である。
3 GiB/swap0/CPU1/pids128、VM 2 GiB/1CPUで順次実行した。全job終了済み。
今回の未使用VM差分4個、88.53 MiBを削除し、base/受入VM/source/package/証跡は保持した。
subjectは3c627db797f2bc7dd6366149800642d07e36b826d1b7ad34cecf4b0e6bc8a496。
判断ADR-0110、証跡distribution/evidence/native-transition/root-reinspection-01/。
私有labはnative-root-reinspection-01。0.3.0 packageと対応sourceはvm-package-05/packagesに保持する。
GitHub公開は未実施。既存minto-dane/niaosは別projectなので上書きしない。公開許可は引き続き有効である。

次はこの実root観測をnative SDKと本番freeze/認可providerへ接続し、予約を維持した実root/boot切替と
段階別復旧を実装する。read-only bind viewだけでは別viewのwriterを止められず、今回の観測は継続的な起動許可ではない。
旧workerで展開したrootは自動移行せず拒否する。ctime/birthtime、未宣言flagsの意味と全MAC policyは未認定。
本番source/consent/quiescence provider、世代GC、全DEB効果、完全置換ISOと全言語翻訳も未完である。

以下は前工程の記録である。

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
