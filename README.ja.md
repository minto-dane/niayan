# Nia OS 開発workspace

7つのAda/SPARKコンポーネントとdistributionを独立Gitリポジトリとして維持し、このworkspaceのsubmoduleで組合せを固定する。[English](README.md)。

**開発ソース／本番未認定。** 実コンパイルと実行試験を導入して不具合を修正している。形式証明と未接続の製品機能は独立した受入条件であり、起動可能な完成OSではない。現在の範囲と結果は[STATUS.ja.md](STATUS.ja.md)。

```sh
make bootstrap       # Debian 13 Distroboxへ依存を導入
sh dev/run-limited.sh make check         # 資源制限付きの全ビルド・登録試験
sh dev/run-limited.sh make private-dbus  # 専用の私有バスによるプロトコル試験
make toolchain       # checksum固定のGNATproveを取得
sh dev/run-limited.sh make proof         # 警告・未証明を失敗にするflow/prove
```

固定コンテナとバイナリ再現性は[開発手順](dev/README.ja.md)、変更と生成物の管理は[CONTRIBUTING](CONTRIBUTING.md)、独立repoの公開順は[GitHub公開手順](dev/PUBLISHING.ja.md)を参照。

| repo | 担当 |
| --- | --- |
| assurance | 信頼・認可・証拠・共有コード・検証基盤 |
| pkgcore | カタログとファイルの変更・復旧・パッケージ意味層 |
| statecore | サービス・クラスタ・健全性・復旧判断 |
| controlcore | 統一管理と公開CLI `nia` |
| configcore | 設定の意味・互換性・生成物 |
| resolvercore | 提案器から独立した候補・証明検査 |
| capsulecore | アプリ世代・同意・権限・broker契約 |
| distribution | 製品仕様・配置・供給入力・出荷条件 |

製品方針はDebian 14 Forkyの認証済み固定DEB入力、installed-stateの正本となるNiaカタログ、永続XFSとFAT32 ESPを維持する。開発環境のDebian 13とは区別する。

製品の正本は[profile](distribution/profiles/nia-os.json)と[contracts](distribution/contracts/)。接続が必要な機能は[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)、[Capsule同意仕様](capsulecore/docs/consent.ja.md)、[継続条件](distribution/docs/continuation.ja.md)に記載する。

旧archiveの説明・hash・試験結果はhistory領域に保全する。過去の成功や未実行という記述を現在の証跡の代わりに使わない。ライセンスは[MIT](LICENSE)。
