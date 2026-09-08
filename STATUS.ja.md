# Nia OS コンポーネント検証状況

2026-09-08。開発ソース／本番未認定。ディストリビューション本体の開発開始前に、既存コンポーネントの実コンパイル、試験、再現性、独立Git管理を整備している。

同日の並列GNATprove実行中にメモリが逼迫し、PCのフリーズと強制再起動が報告された。pkgcore・resolvercore・capsulecoreの全体証明は完了レポートがなく、[中断記録](assurance/evidence/native-development/resource-interruption-20260908/report.json)を保存した。[ADR-0054](assurance/docs/engineering/adr/ADR-0054.ja.md)の資源制限を追加し、小規模試験の後に1件ずつ証明を再開した。前処理を含むプロセスごとの上限に加え、別process groupのソルバーも監視・回収する。ローカルでは一時user scopeによるメモリ3 GiB・swapなし・CPU 1コア分・128プロセスのkernel制限も適用し、各実行前に読み戻す。全7コンポーネントの現行ソースの完全証明はまだ未完。

再起動後、workspaceと全8repoのGitオブジェクト・差分検査は異常なし。最新のDistrobox実行では全499正本Adaファイル・18 CLI・58 Ada試験を検証し、統合103項目が成功した。Python試験554件は543件が通常実行で成功し、root拒否1件・私有D-Bus10件も別実行で成功した。資源guardの15件、kernel設定読戻しの3件を含む。[実行前後のsource subjectが一致した記録](assurance/evidence/native-development/scoped-native-20260908/native/report.json)と[証跡manifest](assurance/evidence/native-development/scoped-native-20260908/manifest.json)を保存している。現行ソースの固定コンテナ再検証・再現性・全体証明は次の受入工程である。

## 修正と管理基盤

初回の全7repoのコンパイル失敗を修正した。Ada予約語・演算子可視性・型とFFI宣言・deferred constant・古い試験APIを修正。部分入力解析でOKが漏れる処理、巨大配列のスタック一括生成、相対パスと試験ディレクトリ準備、子PIDの改行処理を修正した。共有vendor・profile・公開人工fixtureは正本から再生成している。理由と互換性への影響はADR-0053。

各repoの`make test`は中央台帳の全登録Ada mainを実行する生成runnerに統一した。コンパイラ設定変更も再コンパイルする。7コンポーネントとdistributionは独立Git履歴を持ち、workspaceがsubmoduleで固定する。GitHub Actions、固定Debianコンテナ、checksum固定GNATprove導入工具、異なるパスでのバイナリ比較を追加した。

## 検証の区分

取り込み時の全499正本Adaファイルと18 CLI、従来57本のAda試験はDistroboxと固定コンテナで検証した。実LinuxソケットをAdaから呼ぶ試験を追加し、現在の登録Ada mainは58本。送信した子プロセスの資格情報、短い／長いframe、受信FDの解放、誤ったsocket種別の拒否を確認している。最新の全58本のDistrobox実行結果は上記の証跡に束縛している。旧コンテナの成功を現行ソースの成功として流用しない。

Python参照試験、私有D-Bus試験、Ada実行試験、SPARK flow、完全なproveは別の証拠である。GNATprove 16.1の厳格検査で初期化・終了性・契約条件の不足を修正中。未証明の残る状態を成功として扱わない。`make proof`は未証明・警告を失敗にする。

再現性は固定コンテナ・固定依存の下で、異なる作業パスの18実行ファイルをデバッグ情報込みで比較する。OSイメージや異なるarchitectureの再現性を意味しない。生の実行結果は`assurance/evidence/engineering-*/report.json`等にsource hash付きで保存される。旧`consent-integration`と`final-review`は取り込み時の履歴である。

## 製品開発として残るもの

Capsule launcherのpidfd/cgroup/LSMによる実本人確認、native portalと資源のIssue/Withdraw、独立anchor、実GTK/KDE表示とsession切替、kernel sandbox、Flatpak closure、microVM、GPU/Steamの統合は未完。SDK callbackを常にOKで埋めて完成扱いにしない。

full root/catalog-WAL、DEBの必要効果、独立rescue、installer、UKI署名起動、remote management HA、physical fencing、実DB復元、独立trust floor、安全な長期GCは別の製品開発と受入試験が必要。既存の[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)を維持する。

GitHubへのremote設定とpushは未実施。公開先が決まれば[公開手順](dev/PUBLISHING.ja.md)で独立repoを先に、workspaceを後に公開する。
