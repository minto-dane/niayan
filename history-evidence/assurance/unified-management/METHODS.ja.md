# この版の実行証拠の読み方

summary.jsonが今回のsource runへの入口。engineering-*/report.jsonは各回の正確なsource hashと終了値を含みます。
現在summaryが指すrunだけをこの版の根拠にし、旧版・変更前runのPASSを合算しません。
74件は開発検査工具/台帳/参照replay等、44件は準備工具/人工署名/有限DAG抽象/限定filesystem/source確認です。
これらはAdaバイナリの実行、SPARK証明、物理障害、RPM導入、クラスタ統合の試験ではありません。

実行器は変更しないコピーを対象にし、開始前後source hash一致を確認。CIは任意の本番資格情報を渡しません。
GNAT/GPRbuild/GNATprove不在による実際の前提失敗をtoolchain-status.jsonとlogに記録。
ツール不在を「コンパイル成功」「証明成功」に変換しません。

source-diff.jsonは新規30Adaファイル・旧枝復元98Adaファイルを分けます。復元は新規実装や検証成功ではありません。
ZIP検査は別出力package-check JSONに記録し、アーカイブ自身の自己参照hashを避けます。
ファイルハッシュと展開経路は検査しますが、署名済みreleaseや供給元の実ビルド証跡を偽造しません。
