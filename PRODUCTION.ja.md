# niayan 本番化の実装順

2026-09-12 追加実装（未検証）: 確定世代readerを書込実行器から分離し、
実publication/root/CAS予約の下でnative intentと供給認証を作るPkg_Update_Plannerを追加した。
lslpp -l/-L → 同じ管理socket → 非root native catalog reader → 完全sealed応答を接続した。
root-preparation 0.15.0 / management 0.3.0 source。service/socketは配布するが自動起動しない。
新規試験コード・コンパイル・型検査・CIは実行していない。7言語PO原稿を更新し、POT/MO生成も延期。
全managed認可と変更dispatcher、全DEB効果/実boot等は残件。全体完成ではない。
詳細: distribution/native/accepted-catalog.ja.md、ADR-0130。照会の成功をboot/実行の許可にしない。

2026-09-12 追加実装（未検証）: native供給readerの計画時hash/UTCを保持し、
専用非root子pkg_supply_guardによる継続観測をSupervisorの必須経路へ接続した。
同じ計画/世代/元期限と供給bindingを照合し、設定変更・子停止・遅延時はroot効果を遮断する。
root-preparation 0.14.0 sourceへ専用identityと配布構成を追加した。
最新の利用者指示に従いコンパイル/型検査もリリース前へ延期し、新規試験コードは追加していない。
詳細: distribution/native/supply-guard.ja.md。実planner/世代認可/launcherと全体本番化は未完。

2026-09-12 現行実装: 採用要求のgrammarをCLIから分離し、rootで独立解析するtransport、
sealed表示FDを使う計画同意、Supervisorの同一peer必須条件、Ada同意codecを追加した。
management 0.2.0/root-preparation 0.13.0 sourceへ含めたが、本番planner/launcherは未接続。
123原文/7言語assetと対象6 Python moduleのstrict typing、対象Adaコンパイルを完了した。
挙動/VM/形式証明は実行していない。試験コードの量産を止め、意味のあるリリース前CIとレビューへ集約する。

追加指示を反映し、自動Trial/健康失敗による自動旧版復帰を標準経路から外した。
State_Bootは現在の独立anchor、既知の禁止下限、明示的な一回の切替と別の確定認可、限定rescueを要求する。
下限以上でも未知の脆弱性不在を保証しない。健康不足は安定期間の再評価とし、旧版復帰の権限にしない。
カーネルはCVE未掲載を安全とせず、認証済みstable修正/backport対応がなければ判断を保留する。
機関の実環境悪用報告と端末の侵害を分離し、出典付きAuthority_Reports_Wild_Exploitationへ置換した。

インストーラー起動→導入→初回起動→更新→復旧までMicrosoft署名shimのSecure Bootを維持する。
kernelだけでなくinitrd/cmdline/root/設定/modulesまで使用前検証することが必須。
NVIDIA用module-only MOKの暗号化鍵準備工具を追加したが、実鍵生成/登録/署名/ロードは未受入。
実anchor、製品署名、完全検証boot、MOK/native driver、KEV取得providerは未接続。
詳細: distribution/native/plan-consent.ja.md、distribution/boot/README.ja.md、
distribution/native/threat-reporting.ja.md、ADR-0127/0128。全体本番完成ではない。

公開名はniayan、Debian 13 Trixie amd64を最初の対象とする。開発版であり本番認定は未完。
規範は[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)と
[実装保証基準](assurance/docs/engineering/specs/implementation-assurance.ja.md)。
過去の限定試験を現行製品全体の保証へ拡大しない。

2026-09-12の利用者方針: 実装前に処理境界と故障時の状態を設計し、機能をまとまりで実装する。
変更していない入力の再確認、細分化した試験工程の追加を主作業にしない。
重要な機能統合と出荷前を検証の区切りとし、必要な静的検査・形式検証・受入はその区切りで行う。
CIの全体実行と独立コンポーネントの証明は明示的に起動し、文書pushだけで重複実行しない。

最新の利用者指示: コンパイル・型検査も含め、挙動試験・障害試験・全面レビューはリリース直前にまとめる。
いまはAda実行経路とDebian配布構成の実装を優先する。
既存の安全性/ACID/形式保証要件は出荷条件として維持する。新しい未検証実装は本番認定しない。
締切の日付と必要な成果物は問い合わせ中で、実装を止める前提条件ではない。

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

root-preparation 0.11.0とpkg_operator_guardは、既存polkit SDKを専用子で実行する非同期観測を追加した。
最終実DEBで11ケースを受入済み。元期限、順序と返答鮮度を検査し、失効後の再利用を拒否する。
この点観測を計画同意/native guardと実効果の遮断へ結ぶsupervisor、および全runtime保証は残件である。

AdaのPkg_Generation_Executionを追加した。既存の全必須providerを保持したまま、初期化、
最大512batchの進行、二つのnative handoff、独立再検査と予約保持を一つの実行へ組み合わせる。
単一owner/元期限/一試行と失敗後の不確定性を維持する。コンパイル済みで、本番provider/launcherは未接続。
root Supervisorと非blocking controller clientも追加し、実展開中のpolkit失効から遮断/RO化を観測した。
通常fixture統合は成功、取消試験は結果受取で失敗したため全体成功扱いにしない。
修正後再実行、Adaの全経路/形式保証、新しいDebianイメージの受入はリリース直前へ延期した。
