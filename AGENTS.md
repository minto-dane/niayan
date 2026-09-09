# Nia OS — AIエージェントへの引き継ぎ

**Debian 13 KDE開発ISOは起動・導入のVM受入済み。本番・実機は未認定。**
実ISOの対象hashと6項目の受入は`distribution/evidence/debian13/accepted-09/README.ja.md`。BIOS/UEFI/Secure Boot、実日本語入力、オフライン／オンライン導入と再起動、通常ミラーの署名付きAPT索引取得を確認した。ISO 09/10の実バイト列一致、対応ソース1,415組・4,667ファイルの収集・Linux本体補完・コピー後の照合も完了した。`distribution/release/`のソース補完はイメージ構築とは別工程で、内蔵カーネルの本体を省略しない。未接続の独自機能まで完成扱いにしない。
既存コンポーネントの基準実行では、固定コンテナでの全実コンパイル・58 Ada main・555 Python試験・18バイナリ再現性・独立ビルドと、全7repoの厳格なflow/proveを通過した。対象source subjectと証明範囲はSTATUSと実行証跡で確認する。Python試験や模擬D-Busの成功を形式証明・実デスクトップ試験に置き換えないでください。

## 固定した製品方針
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
本番の鍵・policy配備と独立trust floor、契約の意味検証は未完。稼働管理器への接続・対話作成・応答互換性の受入は未完。
多言語インターフェイスはdistribution/docs/decisions/0004-localized-interface.ja.mdに従う。
gettextの実行別UIを使い、操作・署名・catalogと表示言語を分離する。英語原文119件と
日本語・独・西・仏・韓・中国語簡体字・繁体字の7翻訳catalogを実装済み。
第三者訳文レビューは未実施。製品の対象はDebian 13の全言語。distribution/native/debian-languages.jsonの全509 locale組と
installer 78選択肢を扱い、英語fallbackを翻訳完了と数えない。i18n-release-checkは
全言語翻訳が完了するまで失敗を維持する。TUI/GUIとRTL・幅・アクセシビリティは未受入。
追加調査と各コマンドの採用境界は`distribution/native/command-review.ja.md`を参照。

`STATUS.ja.md` → `capsulecore/docs/consent.ja.md` → `assurance/docs/engineering/specs/production-closure.ja.md`。
実行結果はsource hashに束縛した`assurance/evidence/engineering-*/report.json`等。`consent-integration`は取り込み時の履歴。旧evidenceを現行のPASSとして引用しない。

## 次の作業順

全原本の属性・所有権主張を保持するnative索引を追加した。
追加順に依存せず、原本digestとsource ordinalでhardlinkのinodeを区別する。
共有pathの全ownerと属性差、暗黙parent、非directory祖先を保持し、実効ownerは選択しない。
失敗時に候補全体をClearし、全体seal前の候補を公開しない。入力inventoryの破棄後も索引は変わらない。
固定環境でpkgcore全source・4アプリ・21 Ada main、新449・既存payload814 assertionsが成功。
14合成原本35 claim/28 path、13元DEBと大型合成原本の2904 claim/2493 pathを独立tar/CASとhash計算へ照合した。
両集合とも逆順で同じfingerprint。元DEB集合の索引process最大RSSは20,624KiBだった。
対象入力の測定であり、最大4096原本・524288 claim・256MiB名の実負荷受入ではない。
25実行ファイルが二ビルドで一致し、503入力をcheckout・通常・独立・sanitizedコピーへ照合した。
25 ELFの緩和設定、root拒否（新index6 assertions）、ASan/UBSanリンク下449 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。新runtimeはSPARK対象外で、全7repoのproof入力は不変。
最終ソース24工程は成功し、その実行前後subjectは
`d8d464830a283c50c37cfc7c907db77ed80c0a90d90c6f3bce7b20dddca1bd77`で一致した。
索引の原本集合と認可されたresolver集合の一致、package identity/版/architecture、Replaces/Multi-Archとalias、
実効所有権・全効果・CAS pin閉包・稼働catalog/guard・実root/boot・完全置換ISO・全言語翻訳は未完。
詳細はADR-0067、distribution/native/payload-index.ja.mdとpayload-index-01証跡を参照。
次は選択集合・native関係と所有権の意味を、この全claim索引へ接続する。
以下は先行工程の検証境界である。

世代image候補として固定erofs-utils 1.8.6-1のtar直接入力を検証したが、
ACL欠落・PAX小数時刻不一致、前方hardlinkとGNU負時刻の構築失敗により未採用。
17 imageのfsck成功と4組のbyte一致を、属性保持の成功に読み替えない。
runtime・共有contract・proof入力は変更していない。ADR-0066と
distribution/native/generation-image.ja.md、generation-image-01証跡を参照。
失敗出力は論理2TiBの疎ファイルを残す。再帰コピーで実体化しかけた処理を停止して
部分コピーを削除した。失敗成果物はサイズ確認なしにコピー・全hash・圧縮しない。
今回の実験readerは有限の合成image専用で、製品のimage検証器として転用しない。
ソース24工程は成功し、前後subjectは
`8a6ce83352a1d8e86165e2af6428427b5b9e0b67909623ca66685aabd7c2e17d`で一致した。

元DEBのtar内容・属性・リンクを保持するnative SDKを追加した。
独立framingと上流readerを照合し、全体成功後にprivate inventoryを返す。
通常内容と属性blobは既存CASへ保持し、前方hardlink・全permission bit・UID/GID・
正確なPAX時刻・多言語名を扱う。Unicode正規化で別名を同一化しない。
固定環境で全ソース・4アプリ・20 Ada main、新payload814 assertionsが成功した。
C.UTF-8とCのcaller locale、40合成DEBの再生成、11合成入力28 entryの独立oracleが成功。
13元DEBと大型合成DEBの2,904 entry・計166,123,520 byteも独立tar/CAS照合に成功した。
大型100,669,440 byteのnative子process最大RSSは16,640 KiB。当該入力の測定である。
二ビルドの24実行ファイルが一致し、494入力をcheckout・各検証コピーへ照合した。
root拒否3 assertions、24 ELF、ASan/UBSanリンク下814 assertionsも成功した。
Adaと上流libraryのコードは非計測、leak検査は無効。新runtimeはSPARK対象外。
ソース24工程の前後subjectは`32956b52274683d893c1d0c5824d22e45b4ea8f25daa1af78370666a37fa90bc`で一致し、全7repoのproof入力は不変。
採用profile外のglobal PAX・sparse・ACL方言は拒否し、全対応済みとはしない。
既存世代v1にはhardlink・setuid/setgid/sticky・全時刻等を渡せないため、
versionを持つ世代形式・実行器と所有権管理の拡張が次の必要工程である。
全DEB効果・稼働catalog/認可・実root/boot・完全置換ISO・全言語翻訳は未完。

詳細はdistribution/native/deb-payload.ja.mdとdistribution/evidence/native-transition/deb-payload-01/README.ja.md。
過去の検証範囲とhashはSTATUS.ja.mdに保持する。古い記録を現行sourceの成功として流用しない。

元DEBのenvelope/control/metadata/relations/data-streamも読取SDKであり、単独では導入認可でない。
UID 0拒否を解除して稼働OSへ転用しない。Pythonのtrigger参照状態や媒体/TUF cacheは
第二の導入済みDBではなく、observe_success等を本番の成功callbackとして用いない。
論理世代公開SDKはroot.stateのaccepted planとCAS descriptorが権威であり、
generation.nextは未確定の作業ファイルである。Active要求があれば不確定として扱う。
これらの既存SDKと稼働worker、全DEB効果、実mount/bootの接続は未完。

0. 2026-09-08に並列GNATproveで開発PCが高負荷となり、利用者が強制再起動した。重い検証を重ねない。このDistroboxでは`dev/run-limited.sh command ...`の一時user scopeでメモリ3 GiB・swapなし・CPU 1コア分・128プロセスのkernel制限を適用する。flow/proveと選択unit診断はさらに各repoの`ci/proof-guard.py`経由で1件ずつ実行する。制限による失敗を理由に上限を増やす・guardを迂回する・生のGNATproveで再実行することは禁止。制限と残る範囲はADR-0054。通常ビルドも既定JOBS=1を使う。
1. コンポーネント変更は`dev/README.ja.md`に従い固定環境で`make check private-dbus reproducible proof`。配布レシピの変更は`distribution/image/README.ja.md`に従い、`image-check`、影響するDEB/ISOの構築とVM受入を実行する。数学的入力が不変なら同じ証明を重複実行しない。変更時は新しい未証明条件を修正し、証跡を最新の実行入力へ束縛する。既に成功した証拠を更新後の異なる入力へ流用しない。
2. 最新依頼ではパッケージ管理の完全置換とハードニングを優先。native/READMEの未完経路を実装し、新規ISOで更新・障害復旧を受入する。Capsule起動器のpidfd/cgroup/LSM本人確認と`Capsule_Consent_Channel`→Engine→Store→Access_UIも別の未完として維持。SDKの外部関数を「常にTrue/OK」で埋めない。
3. 各資源のnative portal/brokerを実接続。Portalが資源を渡す前にintentを保存。返された資源をユーザー同意と正確に結び付け、取消・失効を実際の遮断まで試験。
4. 研究モデルのroot bootstrap/catalog-WAL、独自DEB意味層、独立復旧起動、独自署名鍵、遠隔HA/fencing、DB復元、独立trust anchor、安全なGCは別の未完として維持する。Debian InstallerのVM受入済みという事実と混同しない。Debian経路の実機・公開運用の確認は別途行う。

## 守る境界
アクセス失敗の監視を権限昇格にしない。生のhost HOME/bus/devicesを公開しない。署名、UI同意、診断、原本の再構成はいずれも単独では実行許可でない。結果不明を未実行にせず、履歴欠落を空の正常状態にしない。revocation完了には資源遮断の観測が必要。コアが疑わしい時は独立rescueへ移る。

## 検査・引き継ぎ
`python3 assurance/ci/engineering.py check`、`lint`、`run-engineering-checks.py --mode source`。
私有D-Busプローブは`capsulecore/ci/test-consent.sh`（専用private D-Bus、実UIなし）。
変更時はADR・要求・危険・故障・テスト台帳、code inventoryを更新。固定vendorは手編集せず確認付き工具を使う。秘密鍵をZIPへ入れない。未実装は未実装と記録し、完全性を宣言するために検査を弱めない。
