# niayan 本番化の実装順

公開名はniayan、Debian 13 Trixie amd64を最初の対象とする。開発版であり本番認定は未完。
規範は[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)と
[実装保証基準](assurance/docs/engineering/specs/implementation-assurance.ja.md)。
過去の限定試験を現行製品全体の保証へ拡大しない。

2026-09-12の利用者方針: 実装前に処理境界と故障時の状態を設計し、機能をまとまりで実装する。
変更していない入力の再確認、細分化した試験工程の追加を主作業にしない。
重要な機能統合と出荷前を検証の区切りとし、必要な静的検査・形式検証・受入はその区切りで行う。
CIの全体実行と独立コンポーネントの証明は明示的に起動し、文書pushだけで重複実行しない。

1. 本番の供給元・鍵・現在方針・世代認可と正確な計画同意を実サービスへ接続する。
   非root SDK、root handoff、保持session、独立観測、取消の実遮断を一本の経路にする。
2. 最終DEB集合の依存・所有権・属性・設定・script/trigger等の効果と復旧条件を実装し、
   実root組立てと単一catalogの原子的な確定へ接続する。
3. 全writer排他、世代slot/保持/GC、容量不足、実boot切替、独立rescue、制御面自身の更新を完成する。
4. 配布済みのinstallp等の採用コマンド、smit/smitty、緊急修正、GUIを同じ管理器へ接続し、
   APT/dpkg/PackageKit等の二重管理を解消したISOを構築する。
5. Capsuleの実起動器・本人確認・portal・同意・資源付与/遮断を完成する。
6. 全対象言語の翻訳とレビュー、入力・RTL・アクセシビリティを完成する。
7. C/FFI/特権runtime等の実装保証、本番MAC/鍵管理、遠隔管理・HA/fencing、
   XFS・DBバックアップ/復元・RAS・長期保存を製品の実構成へ接続する。
8. 最終構成の再現ビルド、必要な障害試験と実機受入、SBOM/対応ソース、署名/更新配信、
   運用・復旧・サポート手順を揃え、本番CIと出荷判定を行う。

旧準備service/socketと専用RPCの撤去は完了。共有Bankと復旧記録は後継で必要なため維持する。
OSの表示名変更だけを理由に内部ABI・保存形式・DEB所有者や原本の履歴を書き換えない。
作成済みの旧APT ISOは比較用であり、niayan名への変更後のISO受入ではない。
自作部分のBSD 3-Clause適用は完了。第三者の許諾と対応ソース義務は別に維持する。

2026-09-12配布checkpoint: 9repo公開、niayan識別情報、12入口のmanagement package、
旧public nia alias撤去、2回の対象を限定したGitHub配布CIは完了した。
最新管理packageは0.1.1、識別packageは0.2.0。稼働管理器への接続完了ではない。

root-preparation 0.9.0は実行中workerの取消監視を追加した。実packageの通常sessionと
途中停止workerへの接続取消・RO化・記録保持を専用VMで受入済み。工程1の本番認可/供給/
計画同意と非root SDKへの接続、全runtimeの形式保証は引き続き必要である。

root-preparation 0.10.0は独立したpolicy/floor原本の明示的な初回配備を追加した。
既存native readerで配備前後を検査し、中断記録を残して上書き/再初期化を拒否する。
実DEBの正常・不正入力・公開途中停止を受入済み。署名や本番の供給authority、時計と
非rollback anchor、方針の管理更新/復旧、認可/計画同意との接続は引き続き工程1の残件である。

再検査handoffの跨UID通信SDKも追加した。元期限と独立期待rootを別operationへ束縛し、
実Ada/C/Pythonの通信と純粋wire validatorを検査済み。実rootを再検査する保持controller、
独立観測、現在認可/供給/同意をresponsive supervisorへ接続する工程1は引き続き未完である。
