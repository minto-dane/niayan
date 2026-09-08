# 今回の検査方法と限界

## 1. 独立参照・ネイティブAPI検査: 22項目 PASS

`current-reference-checks.json`の22項目は、**Adaプログラムを実行した試験ではありません**。
コンテナの独立したPython参照計算とctypesによるネイティブAPI呼び出しで実施しました。
この参照用Pythonスクリプトは配布実装には含めません。配布する実装/試験コードはAdaです。
以下は再構築可能な方法の説明であり、Adaとの同値性を証明するものではありません。

- wire header160バイト、request192バイト、signature64バイトの正規形をbig-endianで構築。
  major2/minor0、kind1..20、予約0、SHA-256を照合。kind256通りと各切断長、旧majorの拒否を参照モデルで検査。
- RFC8032の**公開された試験鍵**で、16バイト署名domainとheaderへのEd25519署名を生成。
  独立暗号ライブラリとnative libsodiumで署名を検証。header160位置の改変とbody192位置のhash不一致を検査。
  署名鍵・fixtureは非本番専用で、信頼ポリシーへ導入してはいけません。
- 256バイトWALを32レコード生成。先頭224バイトに対する末尾SHA-256と前レコードhashを照合。
  32×224=7168位置の改変に対するハッシュ不一致を検査。これはWALの意味的状態遷移や永続化の証明ではありません。
- 3/5ノードの生存/予約/対象組合せ5312通りで、独立した簡略な予算算術を確認。
  実際のState_Budget、故障領域、全State_Topologyコードを走らせた結果ではありません。
- 新しい0700一時ディレクトリ内だけでopenat2/BENEATH/NO_SYMLINKS、statxのABI/mount ID、
  二つのfdのflock競合、fd拡張属性、write/fsync/ftruncateによるサイズ変化を確認。
  ftruncateプローブは回復用CASへの末尾保存プロトコルを試験していません。
- 8つの順序づけられた変更点について独立した単純な状態モデルを確認。
  実I/Oを伴う電源断注入でも、Ada復旧コードでもなく、永続化順序を仮定するモデルです。

archive/curl/xml2の共有ライブラリが見つかったことは依存資材の観測であり、RPM/HTTPS/XMLの全API試験ではありません。
ネイティブプローブは現在のLinux x86-64/glibc環境だけを対象とします。

## 2. ソース/シェル検査: 45項目 PASS

`current-source-checks.json`と各.logを参照してください。三リポジトリの`make check-contract`、
83共有ファイルの名前集合/内容ハッシュ、生成したAdaロック表、shell6本の`sh -n`、Makefileのdry-run、
GPR Mainのファイル存在、JSONの解析、不要なビルド生成物/ソースsymlinkの不在を確認しました。

独立したソース照合器に、1ファイル改変、未知ファイル追加、ファイル欠落を与え、拒否を確認しました。
これは`assure audit-vendors`のAda実行結果ではありません。Adaソースは構文解析/型検査/コンパイルしていません。
`make check-tools`の拒否も記録しましたが、未導入のツールを検出しただけで、コンパイル成功/失敗の判定ではありません。

## 3. 配布整合性

共有契約は`contracts.source.sha256`と`contracts.lock.json`に固定します。
`SOURCE-SET.sha256`は実装/ビルド/fixture/依存宣言の選定集合、`MANIFEST.sha256`はそれ自身を除く配布全体です。
ZIP中央ディレクトリ、CRC、パス、各ファイルのハッシュを作成後に照合します。
これらの無署名ハッシュはドリフト検出であり、供給元を認証する署名や第三者認定ではありません。

## 4. この配布で未実施

Adaコンパイル、Ada単体/統合試験、GNATprove、実signed-RPMコーパス、実systemd/Pacemaker/etcdクラスタ、
実電源断/ENOSPC/fsync失敗注入、物理fencing、DB復旧、Secure Boot/TPM、第三者レビュー、本番認定。
試験ソースと手順は収録しています。`qualification-gap.md`にコンパイル修正以外の実装・接続境界を記載しています。
