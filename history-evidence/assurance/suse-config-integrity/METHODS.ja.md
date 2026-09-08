# この版の検査方法と限界

対象は2026-09-06のSUSE/configuration拡張。環境はSUSEではないLinuxコンテナ。
ホストのパッケージ・Secure Boot・サービス・ネットワーク・GPU・クラスタを変更していない。

## 実行した検査

`source-run/report.json` は実行前後の同一ソース集合に結び付く。
74件: 既存開発台帳・否定試験、44件: 既存統一管理参照/工具、
31件: 新しい設定の独立有限モデル/人工署名/限定getdents64プローブ、
47件: 実際のdistroctl/repo_metadataを人工署名・人工RPM-MD・偽RPMバイトに対して実行。計196件。
重複実行を加算しない。Pythonモデルの成功をAdaコードの成功へ置き換えない。

配布工具の試験は改変・弱いprofile・同一署名主体・期限・rollback世代・別family・
外部metadata参照・XML entities・不正hash・未列挙ファイル・symlink・FIFO・出力上書き等を拒否する。
偽RPMバイトは意図的にインストール不可。元RPM署名/GPG/解決器を検証したとの主張はない。
ネイティブプローブは捨てられる新規ディレクトリ内のLinux64 direntsだけであり、
Ada側のABI/例外/状態機械・サービス回復の検証ではない。

5リポジトリの共有コピーと管理器実装profile、ADR/要求/仕様の参照、
ソース索引、45個のAda test main、5個のRPM specのアプリ対象、Python/shell構文を検査。
字句照合や参照一致は意味的正しさの証明ではない。

## 未実施

別の非特権一時worktreeでbuild/proof入口を実際に起動した。
`build-attempt/`と`proof-attempt/`に記録。ツール不在の項目はNOT_RUN、終了値1。
全Adaのコンパイル、Ada unit/integration/I/O、GNATprove flow/proofは未実施。
実SUSE RPMビルド、全dependency closure、KIWI schema/build、Agama install、
Secure Boot/rescue、RTX3090のsuspend/hibernate、クラスタ分断・電源断・DBrestoreも未実施。

## 証拠の扱い

過去版のevidenceは履歴。現行PASSはこのディレクトリのsource-bound reportだけを参照する。
rootのSTATUSとZIPmanifestの更新は工程の記録であり、source_subjectの範囲は
5リポジトリ+distributionのevidence/build等を除いたファイル集合である。
ソースまたは仕様が変われば新しいrunを要求する。配布後の任意改変に対する署名済み証跡ではない。
人工秘密鍵はテストコードに含む公開の固定種由来。運用鍵として使えず、工具CLIはtest trustを拒否する。
