# Mission Core 拡張版 v2 — 実装・検証状況

作成: 2026-09-06T04:03:06.477324+00:00

## 今回の追加

3リポジトリは独立したビルド定義とMITライセンスを維持しています。
固定vendorコピーを除くAdaソースは181ファイル、
9,129行（コメント/空行/試験/生成ロック表を含む）です。
この行数は品質や完成度の証明ではありません。

| リポジトリ | 実装した経路 |
|---|---|
| pkgcore | RPM署名検査・HTTPS取得・ヘッダー照合付き展開、正規形ファイル計画、CAS/WAL、実ファイル適用・確定・逆順復旧・完了再照合・部分末尾修復 |
| statecore | flat構成三方向マージ、systemd/Pacemaker固定コマンド連携、永続効果記録、etcd mTLS比較更新、共有予算・単調トークンのSDK |
| assurance | v2バイナリ契約、Ed25519要求/証拠、ローカル認可・再送拒否、要求台帳修復、83共有ファイルの固定、否定試験・独立ビルド検証 |

旧来の直接applyコマンドは拒否したままです。署名付きワーカーは実際の副作用を行うコードです。
既存OS全体のRPMDB移行が揃っていないため、pkgcoreの対象は独立管理ルートで、CLIは `/` を拒否します。

## 実施した検査

- 独立参照モデル/暗号fixture/隔離したLinux APIプローブ: 22項目 PASS。
- ソース固定/未知ファイル・欠落・改変/シェル構文/GPR入口/JSON等: 45項目 PASS。
- 配布時に全ファイルmanifest、ZIP内容/CRC/パスを照合。

**Adaプログラムのコンパイル・実行とGNATproveは未実施です。** ユーザー側で引き継ぐ工程として、
ビルド定義、Ada試験、flow/prove、独立リポジトリ適合試験を用意しています。
`runtime/`のLinux/暗号/コマンド境界はAdaの`SPARK_Mode => Off`であり、形式証明済みとはしていません。

## コンパイル修正だけでは完了しない境界

全RPMの依存/trigger/scriptlet/RPMDB所有権移行、サイト固有のトポロジー・物理fencing・業務ヘルス観測、
フリート配布サービスの運用接続、起動チェーン実更新、DB移行/バックアップ、破損時災害復旧/保持期間、
実クラスタと障害注入による受入検証は残っています。成功を装う既定実装や自動保護解除では埋めていません。
任意scriptletをrootで実行するモードは提供せず、明示的な対応契約に限定します。

## 開発の入口

`README.ja.md` → `assurance/docs/build-and-test.ja.md` → 各リポジトリの`make compile-all`、`make test`、
`make flow prove`。接続検証は`assurance/ci/cross-repository.sh`です。

詳しい機能位置は`assurance/docs/implementation-status.ja.md`、未対応境界は`qualification-gap.md`、
実施検査の方法は`assurance/evidence/METHODS.ja.md`、機械可読な状態は各`evidence/qualification.json`にあります。

ソース集合manifest SHA-256: `7f9f6128d27cccd3391aece16f0e83d664379b1412cc19a757e1ac9e2edab441`

本配布は未認定の拡張ソースで、ビルドや単体試験の成功だけで本番認定へ昇格するものではありません。
