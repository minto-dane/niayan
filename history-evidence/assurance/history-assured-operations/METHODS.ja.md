# この版で実施した検査と非対象

## 結果を混同しない

- 独立した参照計算: 13項目。
- Python cryptographyによる公開Ed25519 fixture: 4項目。
- 隔離ディレクトリでのLinux syscall probe: 4項目。
- ソース集合・否定試験・シェル構文・ビルド入口: 46項目。
- 実Adaコンパイル・Ada試験実行・GNATprove: 実行に至らず。

参照計算は状態遷移、permission matrix、checksum、チェーン、削除集合、epoch条件、Base64容量に関する独立した小さなモデルです。Adaを翻訳・実行するものではなく、全状態空間を証明したものでもありません。
署名試験は公開テスト鍵に対して実際に署名/検証し、別domain・別鍵・改変を拒否しました。秘密は存在しない決定的なTEST ONLY fixtureで、本番authorityへ入れてはいけません。
Linux probeは新規0700ディレクトリ内でrenameat2(RENAME_NOREPLACE)、確定衝突後のown-temp削除、fsync、別processのflock、O_NOFOLLOWを実行しました。AdaのMC_FS/MC_Atomicを呼び出した結果ではありません。電源断やディスクのflush保証は未検査です。

## 証拠と再現

`independent-checks.json`と`source-checks.json`に項目・結果・範囲を記録。生成・検査に使用したPythonの全文は `reference-harness.py.txt` / `source-check-harness.py.txt` に監査用テキストとして保存しました。実行時コンポーネントではありません。パスはこの環境の記録なので、別環境で再現する際にはR/Eと隔離一時領域を変更してください。アプリケーション実装・追加単体試験はAda/SPARKです。

独立Base64検査の最初の作成中、16385 byteも16384 byteと同じrounded capacityに入る点をテストの誤った期待値から修正しました。この観測を受け、State_Etcd読込時にもdecoded lengthの明示的検査を追加しました。最終reportは修正後の実行結果です。

## ソース・入口の検査

全3repoの共有集合をchecksum照合しました。各repoの隔離コピーに対し、改変・欠落・未知file・symlink・FIFOを注入し、実check-contract.shが非zeroで拒否することを確認しました。元sourceには不正fileを残していません。
Makeのdry-runは実行予定の構文・入口確認で、コンパイルではありません。GPRのmain-source存在検査は依存解決やAda構文検査ではありません。
GNAT frontendの直接起動は `cannot execute gnat1`、gprbuild/gnatproveの各入口はtool不在で停止しました。全13attemptをログに保存し、PASSへ置き換えていません。

## 未実施

Ada構文/型/リンク/実行、GNATprove flow/safety/functional proofs、実systemd/Pacemaker/etcd、外部anchor、物理fencing、DB restore、長期負荷、ネットワーク分断、電源断、独立security reviewは未実施です。
`make test-control-io`は本当のAda IO試験を実行する入口ですが今回未実行です。そこで使うアンカーはtest doubleで、実非巻戻し基盤を証明しません。

releaseのZIP CRC/path/hash検査は別reportに記録します。配布SHA256は同梱fileの破損検知であり、第三者による署名・由来認証ではありません。
