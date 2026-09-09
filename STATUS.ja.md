# Nia OS 開発・配布検証状況

2026-09-09。Debian 13ベースの起動・導入可能なKDE開発版。実ISOのVM受入を完了し、既存コンポーネントの実コンパイル、実行試験、再現性、独立Git管理も整備した。本番認定・実機認定は行っていない。

## 最新依頼: Niaへの完全置換とハードニング

### 直近の検証

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
