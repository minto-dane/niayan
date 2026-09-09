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

受理済み世代のnative catalog観測をpublication/root/CASの同じ排他区間へ接続した。
Read_Currentと共通の内部処理でaccepted plan・descriptor・manifest pin・journalを検査し、
新しいRead_Current_Catalogが全元DEBからcatalog/payloadを再観測する。最後に状態と期限を再確認する。
失敗はdescriptor/catalog/payloadの旧成功も消す。記録だけのRead_Currentをnative検査済みとは数えない。
返却前に予約を解放するため、観測は長時間の更新許可ではない。Publishの正確なpredecessor比較とmanaged guardを維持する。
固定環境で全source・4アプリ・25 Ada main、公開/復旧試験456 assertions（従来333）が成功した。
二つの合成native catalogと16回の成功観測、既存の拒否/復旧、原本/catalog欠落、root/CAS競合、期限、別root、旧plan拒否を検査。
独立readerが実際のroot.state→accepted plan→descriptor lineage→manifest→catalog→元DEBの関係を通常CIで照合した。
29実行ファイルは独立二ビルドで一致し、725入力をcheckoutと全検証コピーへ照合した。
29 ELF、8本のroot拒否driver（公開driver37 assertions）、ASan/UBSanリンク下456 assertionsも成功。
Adaと上流library本体は非計測、leak検査は無効。全7repoのproof入力は不変、変更runtimeはSPARK対象外。
ソース24工程は成功し、前後subjectは
`4694cfb40880ec35fcb93b8c30fb94d2dbcab4121f091745462ea2aed78a9be7`で一致した。
固定SOURCE_DATE_EPOCHで増分診断の実行ファイルが更新されない挙動を観測し、未採用の記録として保存した。
新規ソースコピーの全build treeでやり直した。dev/READMEの新規build tree必須条件に従う。
試験のauthorityとtree/versionは合成であり、DEB payloadの物理適用ではない。
全OS/最大容量、本番の認証済み予約、CAS pin閉包、保護移行/初期構築、実行phase・所有権/alias・全効果、
実root/boot・完全置換ISO・全言語翻訳は未完。次はcatalogと原本・生成物の保持閉包、実行phaseと本番admissionを進める。
詳細はADR-0072、distribution/native/current-catalog.ja.mdとcurrent-catalog-01証跡。

過去の数値とsource別証跡はSTATUS.ja.mdとdistribution/evidence/native-transition/へ保持する。
以下の既存境界を保つ。

- Catalogは既存NIACSEL1の正規CAS原本であり、Loadは全元DEB/control/payloadを再観測する。
  最終集合receipt、通常更新delta、供給認証、同意、実行phase、所有権、保持閉包は別の検査である。
- 通常更新ではEssential/Protectedのidentity・flag消失を拒否し、検証済みの保護移行経路が別途必要。
  Provides/Replacesを保護identity保持や包括的な上書き権限にしない。
- Payload/indexは全属性と全owner claimを保持するが、実効所有権を選んでいない。
  global PAX、sparse、採用外ACL方言は未対応として拒否する。既存世代v1のfile planへ
  hardlink・全permission bit・負/小数時刻等を切り捨てて渡さず、版付き実行形式で対応する。
- EROFS直接tar入力の固定1.8.6-1実験はACL欠落・時刻不一致等で未採用。
  `/home/nia/devbox/niaos/.work/native-generation-image-01/`には論理2TiBの失敗疎ファイルがある。
  サイズ確認なしの再帰コピー・全hash・圧縮は禁止。以前の展開しかけた部分コピーは削除済み。
- 元DEB SDKは読取/候補構築経路であり、UID0拒否を解除して稼働OSへ転用しない。
  Pythonのtrigger参照状態や媒体/TUF cacheは第二の導入済みDBではない。
  observe_success等を本番の成功callbackとして用いない。
- 論理世代公開の正本はroot.stateのaccepted planとCAS descriptor。generation.nextは作業ファイル。
  Active要求があれば不確定として扱い、欠けたlock/journal/CASを再初期化して正常にしない。

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
