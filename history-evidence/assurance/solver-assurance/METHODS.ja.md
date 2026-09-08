# 実施方法と保証範囲

本版の実行記録はsource-run/とbuild-attempt/、proof-attempt/。
source-runはPython工具・有限参照モデル・人工署名fixture・限定Linux読取と
private temporary file操作を実行した。native libsolv/CaDiCaLは存在せず呼び出していない。
proposer helperの制御logicはFakeSolv APIと非RPMの人工bytesで検査した。
sealed executable試験は実行不能な人工ELF先頭bytesを保存して検査し、実行していない。
証明列テストの推論はPythonの有限参照モデルであり、AdaのRUP/RAT実装を実行した証拠ではない。

source-runの重複実行は件数へ二重加算しない。新しい62件と既存199件、合計261件。
追加のtruth-table列挙やreference redundancy checksは一つのtest method内部の事例。
数量で正しさや完全対応を示すのではない。根拠の粒度は各ログを参照。

build/proofは別の専用作業コピーをUID65534で実行した。source testsは通ったが
GPRbuild/GNATproveが見つからず、Adaの工程はNOT_RUN。各repoのmake compile-allも
ツール前提で失敗した。missing toolsをPASSとして扱わない。worktreeの内容hashは実行記録に含む。

途中の失敗報告も元evidence/engineering-*/に残る。初期source guardがMC_Codecのような
汎用byte codecまで禁止した不備、旧5repo/15tool件数のassert、変更後のmanager fixtureの
再生成漏れを修正した。source-runはそれら修正後の記録。古いPASSは新コードの証拠ではない。

本番のRPMDB・host /・scriptlet/trigger・network/service操作・実クラスタ・fencing・
Secure Boot・GPU suspend・DB復元・電源断を試験していない。実機の秘密情報を取得/記録せず、
private key file、運用署名、native package cacheを配布物に収録していない。

この配布物のchecksumは転送/改変確認用。第三者署名・監査認定・ソース意味の証明ではない。
