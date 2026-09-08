# Nia OS — 同意UI・権限の適用／失効・永続台帳の統合

作成日: 2026-09-07。**開発ソース／本番未認定。起動可能OS・完成sandbox・全面自動復旧ではありません。** Debian 14 Forkyの固定DEB供給、Niaカタログ、永続XFS、7コードベースとdistributionを維持。

## 今回の実装
- Capsule_Consent / Wire / Prompt: 明示要求、起動個体・本人・resource・operation・質問・方針・期限を拘束するSPARK状態機械、112byte入力と640byte状態形式、固定質問のハッシュ。許可は一般UIの承認だけでは発生しない。
- Capsule_Consent_Channel: Linux amd64のprivate SOCK_SEQPACKETからSCM_CREDENTIALS付き要求を受信するAda FFI。余分なFD・不正形式を拒否し、受け取った権利FD/PIDFDを閉じる。launcher側のpidfd/cgroup/LSM登録との照合は必要。
- Capsule_Access_UI: libsystemd経由のGTK/KDE AccessDialog呼出しAda FFI。ホスト側の専用非特権session helper向け。exact owner/UID/必須資格callback/質問hash、結果の型、期限、owner交代を検査。raw busをアプリへ開放しない。現在の表示テンプレートはbounded ASCII。
- Capsule_Consent_Engine: dialogだけの経路とnative portalで同意中に資源が発生する経路を分離。効果前intent、前後の再観測、結果不明を再送しない照合、実撤回の意図／観測／閉鎖を扱うSDK。
- Capsule_Consent_Store: 実MC_FS/MC_Logによるsnapshotとhash-chainの保存、独立anchorの比較更新とread-back、欠落・部分tail・hash不一致・古いanchorを拒否。終端記録の予約。128ticket/8192eventの有界registryで、長期GCは別工程。
- Capsule_Broker.Permit_Consent: 既存sessionと現在のticket・資源・操作を照合する入口。旧User_Confirmedだけを公開APIの許可条件にしない。
- ZIP直下AGENTS.md: 次のAIエージェント向け、固定方針・未完箇所・接続順・検査と禁止事項を短く記載。

## 追加のレビュー修正
MC_Logが読める正常prefixと部分tailを、consent store側では明示的に区別し、部分tailを無視してOpenしないよう修正。正しい名前・ハッシュがあってもmissing snapshotを空状態として補わない。Portalの外部呼出し直前にも現在の状態と期限を再確認。既存の配布gateの固定集合と新しい条件の不一致を検出し、中央定義と契約を同期して回帰試験を追加。

## 実行した検査
|群|固有件数|
|---|---:|
|開発基盤|110|
|統一管理|44|
|設定|31|
|ソルバー|70|
|cohort復旧|50|
|Capsule既存・同意モデル・I/O・private D-Bus|95|
|配布/XFS/gate検査|132|
|合計|532|

一般の非特権source検査で521成功・11skip。skipの内訳はroot拒否1、private D-Bus専用10。専用private D-Busで10件を非特権実行し成功、root拒否1を別contextで成功確認。計532固有試験。再実行・有限モデルの内部組合せを加算しない。private D-Busは実dbus/libsystemdとtest-only peerによるプロトコル試験で、Ada FFI・本物のGTK/KDE表示試験ではない。

**Adaコンパイル・57件のAdaテストmain・GNATproveは未実施。** GPRbuild/GNATproveを確認できず、gccのAda frontend実呼出しも失敗。公式取得先へHTTPSを試したが名前解決で失敗。導入・build/proof試行ログを保持。SPARK state codeと、SPARK_Mode=>OffのLinux/FFI境界を混同しない。

## 未接続・未完成
この版は常駐した完成permission daemonではない。launcherの実本人確認、native portalのNia identity、各資源のIssue/Withdraw、UI claimとrate budgetの永続adapter、独立anchor、実desktop session switchを接続・試験する必要がある。既存のbwrap/AppArmor/seccomp起動器、microVM、全Flatpak取得・closure、GPU/Steamも未完境界を維持。

full root/catalog-WAL、DEBの全必要効果、実rescue/installer/UKI署名起動、remote management HA、physical fencing、実DB復元、独立trust floor、安全な長期GCはコンパイル修正とは別の開発。UI consentはこれらを代替しない。原本・鍵全喪失や侵害されたkernelの自己報告だけから完全回復するとはしない。

現行検査の入口: assurance/evidence/consent-integration/。仕様: capsulecore/docs/consent.ja.md。理由・代替案: ADR-0052。引き継ぎ: AGENTS.md。
