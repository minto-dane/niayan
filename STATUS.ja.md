# Nia OS コンポーネント検証状況

2026-09-08。開発ソース／本番未認定。ディストリビューション本体の開発開始前に、既存コンポーネントの実コンパイル、試験、再現性、独立Git管理を整備している。

## 修正と管理基盤

初回の全7repoのコンパイル失敗を修正した。Ada予約語・演算子可視性・型とFFI宣言・deferred constant・古い試験APIを修正。部分入力解析でOKが漏れる処理、巨大配列のスタック一括生成、相対パスと試験ディレクトリ準備、子PIDの改行処理を修正した。共有vendor・profile・公開人工fixtureは正本から再生成している。理由と互換性への影響はADR-0053。

各repoの`make test`は中央台帳の全登録Ada mainを実行する生成runnerに統一した。コンパイラ設定変更も再コンパイルする。7コンポーネントとdistributionは独立Git履歴を持ち、workspaceがsubmoduleで固定する。GitHub Actions、固定Debianコンテナ、checksum固定GNATprove導入工具、異なるパスでのバイナリ比較を追加した。

## 検証の区分

全499正本Adaファイルのコンパイルと18本のCLIリンク、従来57本のAda試験はDistroboxと新規固定コンテナで成功した。その後、実LinuxソケットをAdaから呼ぶ試験を追加し、現在の登録Ada mainは58本。新試験単体も成功し、送信した子プロセスの資格情報、短い／長いframe、受信FDの解放、誤ったsocket種別の拒否を確認した。最新の全体再試験結果は確定した証跡に束縛して記録する。

Python参照試験、私有D-Bus試験、Ada実行試験、SPARK flow、完全なproveは別の証拠である。GNATprove 16.1の厳格検査で初期化・終了性・契約条件の不足を修正中。未証明の残る状態を成功として扱わない。`make proof`は未証明・警告を失敗にする。

再現性は固定コンテナ・固定依存の下で、異なる作業パスの18実行ファイルをデバッグ情報込みで比較する。OSイメージや異なるarchitectureの再現性を意味しない。生の実行結果は`assurance/evidence/engineering-*/report.json`等にsource hash付きで保存される。旧`consent-integration`と`final-review`は取り込み時の履歴である。

## 製品開発として残るもの

Capsule launcherのpidfd/cgroup/LSMによる実本人確認、native portalと資源のIssue/Withdraw、独立anchor、実GTK/KDE表示とsession切替、kernel sandbox、Flatpak closure、microVM、GPU/Steamの統合は未完。SDK callbackを常にOKで埋めて完成扱いにしない。

full root/catalog-WAL、DEBの必要効果、独立rescue、installer、UKI署名起動、remote management HA、physical fencing、実DB復元、独立trust floor、安全な長期GCは別の製品開発と受入試験が必要。既存の[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)を維持する。

GitHubへのremote設定とpushは未実施。公開先が決まれば[公開手順](dev/PUBLISHING.ja.md)で独立repoを先に、workspaceを後に公開する。
