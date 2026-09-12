# niayan — AIエージェントへの引き継ぎ

**最新指示: 試験・全面レビューはリリース直前へ集約。現在はAdaとDebianの実装を優先する。**
新たなVM試験や反復suiteを開始しない。必要なコンパイルは可。出荷時の形式保証/ACID要件は維持。
Pkg_Generation_Execution（Ada）とroot_supervisor/root_session_clientを追加したが、本番の
供給/世代/同意providerとlauncherは未接続。Debian recipeへroot/供給serviceを同梱し、
開発buildはnocheck、手動配布CIは--releaseとした。サービスの暗黙起動はしない。
root-supervisor-01の通常VMは成功、取消時のworker終了/RO/記録保持を観測したが試験全体は失敗。
fixtureのfork FD継承/後片付けを修正し、再実行を延期した。当前sourceの全体PASSにしない。
最新の実装範囲はPRODUCTION.ja.mdとSTATUS.ja.md。締切の回答は未受領、実装は続けてよい。

**Debian 13 KDE開発ISOは起動・導入のVM受入済み。本番・実機は未認定。**
実ISOの対象hashと6項目の受入は`distribution/evidence/debian13/accepted-09/README.ja.md`。BIOS/UEFI/Secure Boot、実日本語入力、オフライン／オンライン導入と再起動、通常ミラーの署名付きAPT索引取得を確認した。ISO 09/10の実バイト列一致、対応ソース1,415組・4,667ファイルの収集・Linux本体補完・コピー後の照合も完了した。`distribution/release/`のソース補完はイメージ構築とは別工程で、内蔵カーネルの本体を省略しない。未接続の独自機能まで完成扱いにしない。
既存コンポーネントの基準実行では、固定コンテナでの全実コンパイル・58 Ada main・555 Python試験・18バイナリ再現性・独立ビルドと、全7repoの厳格なflow/proveを通過した。対象source subjectと証明範囲はSTATUSと実行証跡で確認する。Python試験や模擬D-Busの成功を形式証明・実デスクトップ試験に置き換えないでください。

## 固定した製品方針
2026-09-12: 公開名はniayan。minto-dane/niayanとniayan-*の8子repoへの公開が明示許可済み。
Niaの内部名称・永続形式と過去の証跡を全面置換しない。既存minto-dane/niaosは別project。
利用者は実装を優先し、検証は機能統合・出荷前の重要なcheckpointへ集約するよう再指示した。
変更のない入力への反復試験や、小さい変更ごとの全体試験を行わない。PRODUCTION.ja.mdを参照。

2026-09-08の最新指示は、Debian 13 Trixieを維持しながらAPT/dpkgを完全置換し、Niaを唯一のパッケージ管理主体にすること。Ubuntu・Kicksecure・公的ハードニング資料を参照し、操作性を維持する。現在のISO 09は旧APT経路の比較基準であり、完全置換は未完。最新判断は`distribution/docs/decisions/0002-native-package-authority.ja.md`、移行工程は`distribution/native/`、セキュリティ基準は`distribution/hardening/`。開発Distrobox/ビルダーのAPT使用は稼働NiaOSの管理主体と別。依存削除・偽Provides・常時成功callback・任意scriptのhost root実行で完成にしない。上流ソースへ独自パッチを当てず、7コンポーネントのAPI・永続形式・検査を強引に変更しない。7リポジトリは独立維持する。旧Forky供給lockや独自UKI等の未受入機能をTrixieで検証済みとしない。

## 最初に読むもの

最新の管理インターフェース判断は`distribution/docs/decisions/0003-management-interface.ja.md`。
Niaが所有する管理機能はinstallp等の採用コマンド体系だけを公開し、公開nia/niactl等の
代替入口を作らない。内部SDKとworkerは別。systemd等の独立した外部工具は元のコマンドを
維持し、互換ラッパーを作らない。emgr/epkgのnative緊急修正を同じcatalog/writerへ接続する
設計変更は許可済み。自作コードと説明は中立名称を使い、原本メタデータ・ライセンス・
hash付き過去証跡は改変しない。現在の12入口のうちepkgのテンプレート作成とemgrの
成果物表示、emgr_download_ifixの署名付きHTTPS取得は動作する。
inutocの媒体索引とinstallp/geninstallの媒体一覧も実装した。詳細はdistribution/native/media.ja.md。
供給認証は上流TUFを使用し、信頼cacheを一つの原子的checkpointとして保存する。
詳細はdistribution/native/repository.ja.md。
独立に用意したpolicy/floorの初回配備とnative意味検査は実装・VM受入済み（下記0.10.0）。
本番鍵の由来・非rollback anchor・更新運用、稼働管理器への接続・対話作成・応答互換性は未完。
多言語インターフェイスはdistribution/docs/decisions/0004-localized-interface.ja.mdに従う。
gettextの実行別UIを使い、操作・署名・catalogと表示言語を分離する。英語原文119件と
日本語・独・西・仏・韓・中国語簡体字・繁体字の7翻訳catalogを実装済み。
第三者訳文レビューは未実施。製品の対象はDebian 13の全言語。distribution/native/debian-languages.jsonの全509 locale組と
installer 78選択肢を扱い、英語fallbackを翻訳完了と数えない。i18n-release-checkは
全言語翻訳が完了するまで失敗を維持する。TUI/GUIとRTL・幅・アクセシビリティは未受入。
追加調査と各コマンドの採用境界は`distribution/native/command-review.ja.md`を参照。

`STATUS.ja.md` → `capsulecore/docs/consent.ja.md` → `assurance/docs/engineering/specs/production-closure.ja.md`。
実行結果はsource hashに束縛した`assurance/evidence/engineering-*/report.json`等。`consent-integration`は取り込み時の履歴。旧evidenceを現行のPASSとして引用しない。

2026-09-12 niayan公開: minto-dane/niayanとniayan-*の8子repoを公開済み。
採用12コマンドをniayan-managementへ配布し、旧public nia aliasはsource/main/artifactから撤去。
内部missionctl/mission_sign、ABI/永続形式は維持。実DEBと固定containerの配置受入が成功した。
本番の認可/供給/計画同意・root session接続、全DEB効果・boot/復旧は未完。
テストは機能統合checkpointと出荷前へ集約。management-packages.ymlが今回の配布CI。run 34716711208はda62319に対して成功。
management 0.1.1/識別0.2.0。全体OSのCI/本番認定ではない。

## 次の作業順

2026-09-12 非同期operator確認: ADR-0125 / REQ-162 / HAZ-149 / FAULT-162。
pkg_operator_guardは既存native polkit SDKを専用root子で実行し、0.11.0のOperatorGuardが
順序付きprivate pipe、peer/子pidfd、元期限と応答鮮度を非同期で検査する。保存grantではない。
最終実DEBの11 polkit case、strict typing、3件の有限制御/FD/UID検査と対応ソース照合が成功。
初回返答の滞留も拒否。証跡はdistribution/evidence/native-transition/operator-guard-01/。
同じpkgcore DEBを再利用し、鮮度修正後はcontrollerだけ再buildした。試験の再起動過多は
実journalのstart-limit-hitで確認してharnessを修正し、製品のpolkit制限は緩めていない。
本番supervisorがこの非同期観測、計画同意、native供給/世代guard、保持root sessionの
実効果遮断を一つのevent loopへ接続する作業が次。全Ada/Python/FFIの形式保証は未完。

2026-09-12 再検査handoff: ADR-0124 / REQ-161 / HAZ-148 / FAULT-161。
Pkg_Root_Handoff.ReinspectとPythonのReinspectionScopeを追加し、元期限と独立期待rootを
224 byteの別要求/応答へ束縛した。一Sessionは準備/再検査いずれか一試行のみ。
実Ada/C/Pythonとkernel credentials/FDの32通信case、strict typing、純粋wire validatorの
CBMC 288 propertyが成功。証跡はdistribution/evidence/native-transition/root-reinspection-handoff-01/。
全transport/FFIの証明ではない。この通信checkpointではpackage版を進めず、実DEB/ISOも再構築していない。
次はこの要求を保持controllerのObserve、独立物理観測、現在認可/供給/計画同意へ結ぶ
responsive supervisor。受信scope/ACKを独立期待値や実行許可へ転用しない。

2026-09-12 supply初回配備: ADR-0123 / REQ-160 / HAZ-147 / FAULT-160。
root-preparation 0.10.0の内部supply_initialize.pyは独立した原本とroot/requestを要求し、
nia-pkgとして既存native readerの--planningで配備前後を検査する。上書き/自動再試行は拒否。
公開後応答前の停止は完了不確定であり、未実行と同一視しない。実DEBの6 VM case、
非root拒否、6単体/有限制御検査、strict typingが成功。全runtime証明ではない。
証跡: distribution/evidence/native-transition/supply-initialization-01/。
本番の供給authority/独立anchor、認可/計画同意、世代guardとroot session接続を続ける。

2026-09-12 root worker監視: ADR-0122 / REQ-159 / HAZ-146 / FAULT-159。
root_sessionのprepare/verifyを型付きroot_worker_monitorへ接続した。実行中にpeer/pidfd/期限を
監視し、未回収leaderを保持したgroup停止、有限pipe/event/回収待ちを行う。0.9.0 DEBへ配布済みsource。
実native worker途中停止後の接続断→終了/RO/記録保持/再要求拒否と、同じDEBの通常sessionを
専用VMで受入した。証跡はdistribution/evidence/native-transition/root-worker-monitor-01/。
8件の試験とstrict typing成功。有限制御探索は全Python/OSの証明ではない。
本番供給/認可/計画同意と非root SDKからこの寿命へ接続する作業が次。完成済みの区切りを反復しない。

2026-09-12の追加方針: 既存という理由だけで旧実装/互換入口/未使用資産を維持しない。
将来の製品に必要な役割、現行利用箇所、代替可否と撤去条件を確認する。
利用者は旧service以外も不要なコード/資産の廃止を許可済み。ACID/権限境界/性能/保守/採用コマンドの
使用感を評価し、中立名称を使う。必要な永続記録/復旧材料を互換実装と同一視して消さない。
必要な比較試験・対応ソース・ライセンス/検証履歴は、現行製品へ残す実行経路と区別する。
無関係の稼働VMや利用者アプリを停止しない。不要と確認した試験cacheだけを明示的に削除する。

2026-09-12の追加必須条件: C等の低水準コードは形式検証と航空宇宙の厳格なコード基準を要求する。
C以外にも影響に応じた基準を適用する。規範はassurance/docs/engineering/specs/implementation-assurance.ja.md。
通常試験/ASanの成功を形式証明とせず、SPARK対象外Ada、FFI、特権Python、シェル/配布/CIを含める。
既存C全体の形式検証・規則適合は未完。本番条件を緩めたり言語変更で回避しない。
小さい関数の証明をOS操作・外部ライブラリ・全実装の証明へ拡大解釈しない。工具不在/unknown/timeoutは未達。
証明harness、環境仮定、実ソースのhashと全未証明条件を保持し、リソース制限を維持する。

2026-09-10の最新指示: 着手済みの共有参照改善の比較・回帰確認を終えたら、本番デプロイを
妨げる未実装部分に集中する。追加の性能研究、試験器の拡張、同じ入力の再検証だけを主作業にしない。
試験は変更境界とリリース判定に必要な範囲へ絞り、検証済みで入力不変の工程は繰り返さない。
以下の一般的な検査手順より、この利用者の最新方針を優先する。
優先対象は実DEBの所有権・全効果とroot組立て、本番認可/供給provider、管理コマンドと実サービスの
接続、起動切替と復旧、完全置換ISOである。全言語翻訳等の既存製品要件も取り消されていない。
SDKと人工fixtureの成功を製品接続完了にしない。

## 継続時の状態

旧root準備service/socket/RPCの撤去はADR-0120 / REQ-158に従い完了した。
共有Bank・永続記録・元の認可/独立観測/実FD/三予約を維持し、制御面のlive更新は拒否する。
0.8.0の移行受入と過去のsource-bound結果はSTATUS.ja.mdおよび
`distribution/evidence/native-transition/root-service-retirement-01/`に保持する。
0.9.0の取消受入はroot-worker-monitor-01を参照し、旧工程の件数を現行全体の保証にしない。
0.10.0は上記初回供給配備、現行0.11.0は非同期operator確認を追加した。
取消runtimeは不変であり同じ試験を反復していない。

2026-09-12 storage整理: 完了済みISO導入VM2台とbuilder guestの/build-03〜/build-09を削除し、
約59.8 GBの実割当を回収。空き約59.7 GiB。現行/build、工具、元ISO、対応ソースと受入記録は維持した。
古いbuild recordはguestの/build/retired-build-records-20260912.tar.xzに保持する。
共有builderの内容はcache整理で変化しているため、過去VMとの全内容同一性を仮定しない。
今後test-suite.pyは全成功後に導入diskだけを自動整理する。明示的な追加調査は--retain-disks、
失敗時はdiskを保持して原因修正後に整理する。一般的な自動cache削除は導入していない。
証跡はdistribution/evidence/development-storage/reclaimed-01/。

本番供給/世代admission、正確な計画同意、root handoff/保持session/独立観測と物理遮断を
非root世代SDKへ接続する作業が次。site供給providerのreaderと明示的な初回配備は実装済みだが、
本番原本のauthority、非rollback floor、署名/認可/保持寿命の接続は未完。許可済みだからと既定allowや
fixture keyで通過させない。C全体/FFI/重要runtimeの形式保証、全writer排他/slot/保持/GC、
実root/boot切替・復旧、全DEB効果、完全置換ISO、全言語はPRODUCTION.ja.mdに従い未完。

重い処理は3 GiB/swap0/CPU1/pids128で逐次。VMは2 GiB/1 CPU。
compile imageは76d5c00d…、QEMU工具imageは7f92f649…で、完全hashと工具/入力は各証跡へ保存する。
KVMは既存の非root VM runner identityを使う。host deviceの権限を変えて回避しない。
無関係のVM/applicationを停止しない。現在の作業・private labは親.work/continuation-state.jsonも参照。
既存minto-dane/niaosは別projectなので上書きしない。
