# Nia OS 開発・配布検証状況

2026-09-08。Debian 13ベースの起動・導入可能なKDE開発版。実ISOのVM受入を完了し、既存コンポーネントの実コンパイル、実行試験、再現性、独立Git管理も整備した。本番認定・実機認定は行っていない。

コンポーネント受入時（workspace commit `baba69f`）のsource subjectは`2d5b48e6fa437795af02df4943ea1b365ddad62185a88a5d394d201a45958c3d`。固定コンテナでのnative受入と、全7コンポーネントの厳格なSPARK flow・全体証明を完了した。

その後、利用者の指示によりDebian 13の実配布構築へ進んだ。新しいビルド工具・パッケージングは[配布構築手順](distribution/image/README.ja.md)、従来の独自カタログモデルとの関係は[設計判断](distribution/docs/decisions/0001-debian13.ja.md)。コンポーネントの証明と、次のISO受入を別々に記録する。

## Debian 13の実イメージ

`niaos-0.1.0-amd64.hybrid.iso`（3,637,100,544 bytes）のSHA-256は`d4c18dc0e2be653bf11a04db40db95ca0353322010133e068dda274bd4aa314b`。KDEの実Live環境でBIOS・UEFI・Secure Boot、日本語の実入力と保存を確認した。新規仮想ディスクへのUEFIオフライン導入、BIOSオンライン導入、それぞれの再起動と導入済みディスクのSecure Bootも成功した。Liveとオンライン導入先で、通常Debianミラーの署名付きAPT索引を実取得した。[6項目の一括受入と構築記録](distribution/evidence/debian13/accepted-09/README.ja.md)。

上流kernel・systemd・KDE・live-build・Debian Installerと、既存7コンポーネントのソースは改変していない。独自DEB、正式なchroot hook、KConfig、APT/GRUB設定の追加で統合する。試作で見つかった識別情報、Wayland日本語入力、bootstrapのCA証明書、インストーラーのHTTPS親ミラーとミラー設定モジュールの問題を配布レシピで修正した。失敗・中断記録も[evidence/debian13](distribution/evidence/debian13/)に残す。

独自DEBの構築で58 Ada mainを実行し、再ビルドした19 DEB（デバッグ情報を含む）と8組16ファイルのnative source packageが全件一致した。同一入力からの独立した2回のISO構築でも、SHA-256と実バイト列が一致した。[09/10比較](distribution/evidence/debian13/reproducibility-09-10/README.ja.md)。対応ソースの保管は別工程で確認する。GitHub ActionsのDEB構築workflowも用意したが、GitHub上では未実行。

オフライン導入で「ミラーを使わない」を選ぶとCDソースだけを保持する。オンライン導入は通常ミラーを設定する。実機のGPU・音声・無線・サスペンド、暗号化導入、対話GUIの全操作、GNOME/serverイメージは未受入。Live終了時の読み取り専用メディアのunmount警告も実ログに保持する。

## 実コンパイル・実行試験・再現性

固定したDebian 13.6 amd64 imageと2026-09-07の署名済みsnapshotで、全499正本Adaファイルをコンパイルし、18 CLIをリンク、全58登録Ada mainを実行した。統合103項目が成功し、実行前後のsource subjectは一致した。Python参照・工具・プロトコル試験555件は、通常実行の544件と、別contextのroot拒否1件・私有D-Bus10件を合わせて成功した。

署名付きDEB人工fixtureのGPG依存不足を修正した。現在はgpg・gpg-agent・gpgconf・gpgv・dpkg-debを必須とし、不足時は統合検査を開始前に失敗させる。今回の固定コンテナでは当該fixtureの省略はない。root拒否試験はGitHub Actionsでも専用コンテナで実行する設定を加えた。GitHub上での実行自体はまだ行っていない。

異なる長さの作業パス、入力mtime、JOBS=1/2、UTC0/HST10で2回ビルドし、18実行ファイルがデバッグ情報込みで完全一致した。また、各コンポーネントを兄弟repoなしで別々にmountし、全7repoのcompile-all・build・testを実行して成功した。以前のビルド生成物は持ち込んでいない。

[固定コンテナ受入の概要](assurance/evidence/native-development/current-fixed-container/report.json)、[全native検査](assurance/evidence/native-development/current-fixed-container/native/report.json)、[再現性](assurance/evidence/native-development/current-fixed-container/reproducibility/report.json)、[独立ビルドを含む実行一覧](assurance/evidence/native-development/current-fixed-container/pipeline-report.json)を保存している。CIとroot試験の説明だけを受入後に追加した差分は[別記録](assurance/evidence/native-development/current-fixed-container/post-run-workspace-changes.json)にある。コンポーネント・ビルド・工具・package入力は変更していない。

## SPARKの証明

GNATprove 16.1をchecksumで固定し、全unit対象の厳格なflowとlevel 4 proveを使う。未証明・警告は失敗にする。次の件数は各repoの固定vendorも含むため重複する。

| コンポーネント | 全体証明 |
| --- | ---: |
| assurance | 1,809項目 成功 |
| pkgcore | 3,943項目 成功 |
| statecore | 3,592項目 成功 |
| controlcore | 2,030項目 成功 |
| configcore | 2,292項目 成功 |
| resolvercore | 2,499項目 成功 |
| capsulecore | 2,135項目 成功 |

全7repoについて、現在の数学的入力集合と完了実行の集合が完全一致することを確認している。pkgcoreの実行時workspace subjectは`091ce3fc…`、assurance・statecore・controlcore・configcore・resolvercoreは`330e7a97…`、最後に修正したCapsuleは現在のsubjectである。文書や試験工具の依存変更だけを理由に、同じ証明を重複実行していない。[全7repoの照合結果と完全な実行証跡](assurance/evidence/native-development/current-component-proof/report.json)を保存した。中断したworkspaceコマンドを成功に置き換えず、完了した各repoの結果を照合している。

Capsuleの前回の全体実行では、権限の積集合とpromptの書込位置に10件の未証明が残った。点ごとの積集合・Subsetの契約、容量とcursor進行の契約・不変条件を追加した。選択範囲61項目の厳格証明に続き、全能力の16組合せ、最小・最大長の独立digest基準値、高い配列添字、無効入力のAda試験を通過し、最後の全体証明も成功した。途中の[選択証明と実行試験](assurance/evidence/native-development/scoped-capsule-bounds-20260908/report.json)は、全体証明と分けて保存している。

State_Cluster_Safetyの自動展開中のツール内部エラーも保存し、旧・新両構成の過半数を維持するループ不変条件を追加した。その後のstatecore全体証明は成功している。修正と互換性の理由は[ADR-0053](assurance/docs/engineering/adr/ADR-0053.ja.md)。

## 開発環境とGit管理

7コンポーネントとdistributionは独立Git履歴を持ち、workspaceがsubmoduleのcommitを固定する。固定vendor・profile・人工fixture・独立CI/test runnerは正本から再生成する。手順は[開発環境](dev/README.ja.md)と[公開手順](dev/PUBLISHING.ja.md)。

高負荷による強制再起動を受け、重い検証は1件ずつ実行する。ローカルは一時user scopeでメモリ3 GiB・swapなし・CPU 1コア分・128プロセスをkernelで制限し、実行前に読み戻す。固定コンテナ内部からも同じ値を確認した。証明はさらに単一起動lock、子孫監視・回収、プロセスごとの上限、実時間上限を適用する。上限到達を成功にしない。詳細は[ADR-0054](assurance/docs/engineering/adr/ADR-0054.ja.md)。

## 製品開発として残るもの

Capsule launcherのpidfd/cgroup/LSMによる実本人確認、native portalと資源のIssue/Withdraw、独立anchor、実GTK/KDE表示とsession切替、kernel sandbox、Flatpak closure、microVM、GPU/Steamの統合は未完。SDK callbackを常にOKで埋めて完成扱いにしない。

研究モデルのfull root/catalog-WAL、独自DEB意味層、独立rescue、UKI署名起動、remote management HA、physical fencing、実DB復元、独立trust floor、安全な長期GCは別の製品開発と受入試験が必要。今回のDebian経路ではAPT/dpkgとDebian Installerを採用し、研究モデルの独自executorを有効化しない。既存の[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)は、この独自機能群の未完条件として維持する。

GitHubへのremote設定とpushは未実施。公開先が決まれば[公開手順](dev/PUBLISHING.ja.md)で独立repoを先に、workspaceを後に公開する。
