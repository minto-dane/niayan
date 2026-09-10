# Nia OS 開発workspace

7つのAda/SPARKコンポーネントとdistributionを独立Gitリポジトリとして維持し、このworkspaceのsubmoduleで組合せを固定する。[English](README.md)。

現在は[APT/dpkgをNiaへ完全置換する工程](distribution/native/README.ja.md)と
[操作性を維持するハードニング](distribution/hardening/README.ja.md)を進めている。
以下の受入済みISOはAPT版の比較基準であり、完全置換後の製品ではない。

**Debian 13ベースの起動・導入可能なKDE開発版。本番未認定。** 実ISOでBIOS・UEFI・Secure Boot、日本語入力、オフライン／オンライン導入と再起動、署名付きAPT索引取得を確認した。独立した2回のISO構築がバイト単位で一致し、対応ソースの収集とコピー後の照合も完了した。[配布受入](distribution/evidence/debian13/accepted-09/README.ja.md)と[構築手順](distribution/image/README.ja.md)。

既存コンポーネントは全499正本Adaファイルの実コンパイル、58 Ada main・555 Python試験、全7repoの厳格なSPARK flow・level 4証明を通過している。18実行ファイルの再現性と独立ビルドに加え、配布向け19 DEBも再ビルドで一致した。未接続の独自製品機能、実機試験と各証跡の対象範囲は[STATUS.ja.md](STATUS.ja.md)に記載する。

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
| controlcore | 統一管理契約と内部controller |
| configcore | 設定の意味・互換性・生成物 |
| resolvercore | 提案器から独立した候補・証明検査 |
| capsulecore | アプリ世代・同意・権限・broker契約 |
| distribution | 製品仕様・配置・供給入力・出荷条件 |

実配布のベースはDebian 13 Trixie。上流ソースの無改変と保守性を維持し、稼働OSのパッケージ管理をNiaへ一元化する。[最新判断](distribution/docs/decisions/0002-native-package-authority.ja.md)と、旧APT基準版の[配布構築](distribution/image/README.ja.md)を区別する。

配布ビルドの入力は[image](distribution/image/)と[packaging](distribution/packaging/)。従来の[profile](distribution/profiles/nia-os.json)と[contracts](distribution/contracts/)は独自カタログの研究モデルとして保存する。接続が必要な独自機能は[本番接続表](assurance/docs/engineering/specs/production-closure.ja.md)と[Capsule同意仕様](capsulecore/docs/consent.ja.md)に記載し、通常のDebianデスクトップが起動することと区別する。

旧archiveの説明・hash・試験結果はhistory領域に保全する。過去の成功や未実行という記述を現在の証跡の代わりに使わない。workspace固有コードのライセンスは[BSD 3-Clause](LICENSE)。Debianパッケージとvendorには、それぞれのライセンスが適用される。
