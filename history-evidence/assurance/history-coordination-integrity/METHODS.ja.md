# 今回の証拠と限界

edition: coordination-integrity-source-2026-09-06

## 実行したもの

`independent-checks.json`: 独立Pythonモデルと公開fixture等50項目。内訳は参照38、暗号9、Linux probe1、source-data2です。
3対象の8部分集合と小さな比較更新モデルの6順列を調べます。これは有限のモデル検査で、Ada・etcdの全振る舞いを証明するものではありません。
署名検査はcryptographyのEd25519実装を利用しました。運用Adaランタイムのlibsodium呼出し・FFIを実行したものではありません。
Linux probeはprivate一時directoryでflock/rename/fsyncを実行した一検査です。電源断・ストレージ故障・永続化の証明ではありません。
fixtureは独立encoderで作った合成データで、実etcdの応答収集ではありません。

`source-checks.json`: 62項目。実際の3repo契約検査、改変/欠落/未知ファイル/symlink/FIFO/manifest FIFO/Unix socketの拒否、シェル構文、GPR main存在、dry-run入口、profile一致、ソース配線などです。
テキストの存在検査は意味的正しさの証拠ではありません。FIFOを含む否定試験はprivate copyの実CIへ投入しました。
発見されたFIFO hash待機問題を修正した後の結果です。待機を終了するtimeoutを「安全な拒否」と数えていません。

## 実行できなかったもの

各repoでmake compile-all/test/flow/proveを実際に試行し、gprbuild/GNATproveがないため停止しました。
GCCのAda frontend試行もgnat1不在で失敗しています。ログを削除せず`*-attempt.log`へ保存しました。
これらは全てNOT_RUN_TOOLCHAIN_UNAVAILABLEでありPASSではありません。

実Ada単体試験、native file-engine/etcd/barrier統合、ライブのTLS/RBAC/fencing、サービス停止、分断、再起動、電源断、災害復旧、GNATproveは未実施です。
SPARK契約・postconditionは証明目標であり、成立済みと扱いません。

## 参照検査の再現

Pythonは運用コンポーネントではなく、独立検査の記録です。非特権・隔離したビルド環境で、Python 3とcryptographyを用意してください。
証拠を含む元配布をそのまま書き換える必要はありません。作業コピーを作り、出力先もそのコピーに限定してください。

```sh
python3 assurance/evidence/reference-harness.py.txt . /tmp/mc-reference-result.json
python3 assurance/evidence/source-check-harness.py.txt .
```

二つ目は作業コピー内assurance/evidenceにログを書き、native build入口を試行します。既存サービス/clusterへの接続やインストールはしません。
共有検査が前提とするのは固定されたprivate workspaceです。同時に攻撃者がファイル型を入れ替えられるsource treeに対する完全なTOCTOU保護ではありません。

## 過去結果

`history-assured-operations/`、`history-expanded-v2/`、`history-resilience-v3/`は以前の版の履歴です。
その版のprofile、source-set、検査件数は今回のコードの証拠ではなく、合算もしていません。
