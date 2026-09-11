# GitHubへの公開

既存方針に合わせ、7コンポーネントとdistributionは独立repo、直下はcommitを固定する統合workspace repoである。remote設定・GitHubアカウント作成・pushはまだ行っていない。

2026-09-10の利用者指示により、必要時に`gh`で`minto-dane`名義のrepository作成とReleases利用が
許可されている。`gh api user --jq .login`で同名の認証を確認した。2026-09-11の確認では`minto-dane/niaos`は既存の非公開カーネル開発repoであり、
このworkspaceとは異なる内容だった。既存repoは保持し、このworkspaceは別名（候補`niaos-distribution`）を使う。
子repoは同ownerの現行ディレクトリ名を候補とし、作成前に衝突を確認する。既存repoを上書き・強制pushしない。
公開が必要になるまではローカルで整備を続け、空repo作成やrelease番号だけを完成としない。

自作部分は[BSD 3-Clause](../LICENSE)、適用範囲は[LICENSING.md](../LICENSING.md)。
`make license-check`で現在の表記と正本/vendorのnoticeを検査する。過去のMIT許諾、第三者原本、
Debian packageのcopyrightと対応sourceの配布義務は維持する。BSD表記だけを理由に第三者成果物を転載しない。

同じGitHub ownerの下に、まず`assurance`、`pkgcore`、`statecore`、`controlcore`、`configcore`、`resolvercore`、`capsulecore`、`distribution`の空repoを作る。各ディレクトリのmainを対応するrepoへpushしてから、workspace repoをpushする。`.gitmodules`の`../assurance`等はworkspaceのremoteと同じownerの兄弟repoへ解決される。別名・別ownerに配置する場合は`.gitmodules`を明示的に修正して`git submodule sync --recursive`を行う。

```sh
# 各コンポーネント内で、実際のownerに置き換える
git remote add origin git@github.com:OWNER/assurance.git
git push -u origin main
# 8つの子repo公開後、workspace直下でもoriginを設定してpushする
```

新規利用者は`git clone --recurse-submodules <workspace-url>`で取得する。既存cloneは`git submodule update --init --recursive`で固定版へ合わせる。`git submodule update --remote`は検証済みの組合せを変更するため、通常の取得手順には使わない。

CIはcommit SHAで固定したGitHub Actionsとchecksumで固定したproof toolchainを使う。native・proofの結果を別々に確認する。本番資格の未完条件はSTATUSに残し、native成功だけを根拠にrelease認定しない。
非公開repoとして配置する場合、子repoのcheckoutに必要な専用のread-only認証を配備してCIを受入する。
開発端末の広い権限を持つ認証情報をCI secretへ転用しない。現在はremote CIの実行結果はない。

Debian配布物は[構築・記録・対応ソース収集の手順](../distribution/image/README.ja.md)に従う。Gitにはレシピと小さな検査記録を置き、ISO・DEB・対応ソースアーカイブは別の成果物保管先へ置く。公開前に実在する管理者連絡先、更新先、署名と保管責任、サポート範囲を設定する。現在は開発版であり、NiaOS独自の公開APT更新チャネルは提供していない。

GitHubへ送る前に、現在treeだけでなくpushするGit履歴、公開試験鍵と秘密情報の区別、
submoduleの到達可能なcommit、大容量blobと成果物の対応sourceを確認する。
公開試験fixtureの鍵は本番の署名へ使わない。過去の試験用URLを製品の更新先へ流用しない。

Releasesは先に対象commit/tag、版、成果物manifestとSHA-256、対応source、release notesを固定する。
未完成の開発成果物を公開する場合はdraft/prereleaseとして明記し、未完機能と既知の制約も添付する。
`gh release create <tag> --repo minto-dane/niaos-distribution --verify-tag --draft --prerelease --notes-file <notes>`で
review可能なdraftを作り、対象と添付内容を照合してから公開する。本番資格の未完条件が残る間は
stable releaseやAPT完全置換済みという表示をしない。同一tag/版のassetを異なるbytesへ上書きしない。

現在の`0.1.0+git<commit>`は初期開発スナップショットの識別子であり、Git hashの大小をリリース順に使わない。公開更新ではコンポーネントのパッケージ版とintegrationのchangelogに増加する版を割り当て、生成済みDEBの新旧Versionを`dpkg --compare-versions NEW gt OLD`で確認する。同じ公開済み版へ異なる内容を上書きせず、新しい版としてビルド・受入・ソース保管を行う。[Debian PolicyのVersion規則](https://www.debian.org/doc/debian-policy/ch-controlfields.html#version)。
