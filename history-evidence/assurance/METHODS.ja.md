# 今回の実施方法と検証の限界

Edition: distro-foundation-source-2026-09-06。履歴はhistory-*に分離しており、以前のログを今回の実行として数えません。

|報告|今回実行した検査|結果|
|---|---|---|
|prior-reference-regression.json|前版の独立参照計算・署名fixture・隔離Linux APIプローブを、今回のツリーへ再実行|50 PASS|
|source-checks.json|3リポジトリのソース固定、欠落・未知ファイル・FIFO/socket/symlink否定検査、shell構文、GPR入口、make dry-run等|62 PASS|
|distro-reference-results.json|今回の独立参照計算、31種類の人工資格証拠、旧停止状態のgolden再構築、実procfs/openat2読取り|32 PASS|
|distro-source-results.json|新しい接続点のsource wiring、helper構文、RPM specの配備範囲、systemd定義の隔離構文検査|24 PASS|
|maintenance-tool-results.json|独立した一時作業ツリーでロック・公開fixtureの再生成、変更検出、再照合|9 PASS|

保守試験は他の検査を一時コピーで再実行するものも含みます。項目数は独立した保証の個数でも品質スコアでもありません。

## 実行していないもの

Ada本体のコンパイル・実行、GNATprove、RPMバイナリのビルド・導入・消去、systemdサービスの起動、NetworkManagerへの操作、物理fencing、etcdクラスタ、Secure Boot起動、電源断・DB復元は実行していません。コンパイラと証明工具の不在で停止したログは別に保存しています。

参照PythonはAdaから抽出した実装ではなく、仕様の一部を別実装したものです。実装が同じ性質を持つことの証明にはなりません。source wiring検査も文字列・配線の検査であり、機能的正しさを判定しません。

## Linuxとsystemdの限定検査

procfsのboot_idがst_size=0でも実際には37byteを返すこと、同じ固定パスをopenat2の制約下で上限付き読取りできることを、このコンテナで確認しました。カーネルやホストそのものの信頼性の証明ではありません。
systemd-analyze verifyはオフラインで使い、付属observer unitには一時root内でExecStartパスを満たす/usr/bin/trueのstubを置きました。stubもunitも起動していません。unitの実隔離、resource enforcement、DynamicUser、LSMの動作試験とは別です。

## 人工的な署名fixture

fixtures/qualification-v1のPassedは人工入力です。実際のコンパイル・証明成功を表しません。公開テスト鍵はci/regenerate-public-fixtures.pyから誰でも再生成でき、本番で使用不可です。fixtureと実資格証拠は別ディレクトリ、別目的です。

## 再実行

```
python3 assurance/evidence/history-coordination-integrity/reference-harness.py.txt . /tmp/mc-prior-reference.json
python3 assurance/evidence/distro-reference.py.txt . /tmp/mc-distro-reference.json
python3 assurance/evidence/distro-source-check.py.txt . /tmp/mc-distro-source.json
```

ビルド環境を用意した後に各repoのmake compile-all/build/test/flow/prove、statecoreのtest-host-io、assuranceのci/cross-repository.shを実施してください。成功後も、31項目の実機／運用資格条件は別に審査が必要です。
