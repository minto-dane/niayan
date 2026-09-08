# Mission Core — expanded source set / wire contract 2.0

本配布は `pkgcore`・`statecore`・`assurance` の独立した三つのコードベースです。
前版の提案型状態機械に加え、**ファイル/CAS/WAL実行、署名付き要求の永続受理、systemd/Pacemaker実コマンド、etcd比較更新、取得・RPM署名検査・展開**を実装しています。

**Adaコンパイル・Ada試験・GNATprove・実クラスタ認定はこの配布環境では未実施です。**
本版のコードをコンパイルして修正する工程と、本番稼働の認定は別です。実装の存在を、完全性や全障害下の正しさの証明とは表示しません。

## 三つの責任

| リポジトリ | 主な成果物 | 境界 |
|---|---|---|
| `pkgcore` | `pkgctl`, `pkg_worker`, RPM解析/取得/展開、ファイル計画、CAS、変更/復旧実行器 | 明示的な管理対象ルート。任意scriptletとRPMDBを無条件に採用しない |
| `statecore` | `statectl`, `state_worker`, 構成検査/三方向マージ、systemd/Pacemakerアダプター、etcd予算調整SDK | 業務ヘルス/物理fencing/トポロジーの観測責任はサイト側 |
| `assurance` | `assure`, 署名/認可/再送制御、契約固定、独立ビルド適合試験、検証プロジェクト | コンパイラ/証明器、Linux/ネイティブライブラリは別途信頼・検証対象 |

`assurance/src` と `assurance/runtime` を、他の二つへ **固定コピー**として配置しています。
シンボリックリンクや自動的な最新版取り込みではありません。ファイル集合とハッシュ、実行可能ファイル間のgolden vectorを照合します。独立配布時も `vendor/contracts` を維持してください。

## 今回つないだ実行経路

1. 署名付き受入grant → HTTPS・ハッシュ/サイズ制限 → CAS → 固定した`rpmkeys`による検査 → RPMヘッダー照合付きlibarchive展開。
2. 明示的な前後像の計画 → 認証・認可された要求 → クラスタ予約/静止証拠 → WAL → 一時ファイル → 属性照合 → 同一ディレクトリ内の公開 → 再観測 → 確定。
3. 同じ要求の再送 → 永続受理記録を確認 → **副作用を再実行しない**。不明な結果は、新しい認可済みの復旧/再照合要求へ。
4. systemd/Pacemaker操作 → 実行前の観測 → 意図の永続記録 → 固定ELFをシェルなしで実行 → 再観測。戻り値だけを業務ヘルスと扱わない。
5. 共有更新枠 → etcdの比較更新。未完了の予約をTTLだけで解放せず、再参加または隔離の認証済み証拠を要求。

## 初めに読むもの

- `assurance/docs/implementation-status.ja.md` — 実装/接続/未認定の区別。
- `assurance/docs/build-and-test.ja.md` — ビルド・否定試験・独立リポジトリ検査。
- `pkgcore/docs/operations-v2.ja.md` — RPM取得、計画生成、実適用、復旧。
- `statecore/docs/cluster-v2.ja.md` — 所有権、systemd、Pacemaker、etcd予算。
- `assurance/docs/protocol.md` — **破壊的変更のv2**、署名、証拠、再送。
- `assurance/docs/proof-boundary.md` — 証明対象、外部前提、未証明の境界。
- `assurance/docs/qualification-gap.md` — コンパイル修正では埋まらない残課題。
- `assurance/evidence/METHODS.ja.md` — 今回実施した検査と、その限界。

## ビルド入口

対応するGNAT/GPRbuild/GNATproveとネイティブ開発ライブラリを別途用意してください。
通常の非特権ビルドユーザーで、展開先の各ディレクトリから実行します。

```sh
make -C assurance build test
make -C pkgcore build test
make -C statecore build test
./assurance/ci/cross-repository.sh
make -C assurance flow prove
make -C pkgcore flow prove
make -C statecore flow prove
```

全SDKユニットのコンパイルには各リポジトリで`make compile-all`を実行します。
`qualification` / `release-gate` は認定証拠の不足を示して終了します。これらを通すためだけに
証拠の値や`Build_Qualified`を変更しないでください。**ワーカーの実行コードと認定状態は別です。**

## 保持した安全上の制約

通常の`pkgctl apply`等の旧来直接操作は拒否します。実操作は`pkg_worker` / `state_worker`へ、
保護されたローカル方針と署名付き要求を介して行います。新ワーカーは実際に変更するコードです。

初期CLIプロファイルは管理対象ルート`/`を受理しません。既存OS全体のRPMDB移行が未完成であるためです。
これは単なるデモスイッチではなく、未対応の所有権モデルを拒否する制約です。
`/srv/mission/...`等の専用ルートに対する実際のファイル変更と、明示的に構成した実サービス/クラスタ操作が対象です。

全RPMを自前ビルドする必要はありません。ただし任意パッケージを無条件に導入できるわけでもありません。
受入メタデータ・効果契約・管理ファイル計画の作成と維持は必要です。ネイティブRPMDBの書き込み、
任意scriptlet/trigger、起動更新、データベース移行、実機fencingは、それぞれ未完成/サイト固有の境界として明示しています。
