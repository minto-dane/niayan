# 今回の実行方法と証拠の境界

ソースsubject: `bb1f97e34ceb743adce2012fcdfebd23673ed42b719c48fe13d376844f452ee7`。入力ZIP: `mission-core-distro-foundation-source-2026-09-06.zip`。

`python3 assurance/ci/run-engineering-checks.py --mode source`を実行しました。
詳細は`../engineering-hft01u2a/report.json`とハッシュ付きログにあります。
開発検査・参照モデルのPython unittest 60件、3repo共有ソース照合、syntax/doc-link lintを実行しました。
参照モデルはAdaを呼び出しません。write/fsync/fencing等の実装保証を証明する試験ではありません。

`python3 assurance/ci/engineering.py check`は要求/ADR/危険/故障計画/全GPR test main/API在庫を検査します。
`python3 assurance/ci/engineering.py lint`はPython AST、shell構文、Markdown local参照を検査します。
Ada 7ファイル追加、11ファイル変更（tests/generated込み、vendor除外）はchanges.jsonに列挙します。

この環境にgprbuild/gnatproveがないため、make compile-all/flow/proveはmissing-tool gateで停止しました。
実際の終了値とログはcompiler-gates.jsonへ保存しています。未実施を成功へ読み替えていません。
Adaの機能試験33mainは登録しただけで、今回はいずれも未実行です。

文書とソースを変えたらsubjectは変わります。過去版evidenceを現行版へ転記しないでください。
このJSONやハッシュ自体は、独立した署名主体による本番資格証拠ではありません。
