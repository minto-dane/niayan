# GitHubへの公開

既存方針に合わせ、7コンポーネントとdistributionは独立repo、直下はcommitを固定する統合workspace repoである。remote設定・GitHubアカウント作成・pushはまだ行っていない。

同じGitHub ownerの下に、まず`assurance`、`pkgcore`、`statecore`、`controlcore`、`configcore`、`resolvercore`、`capsulecore`、`distribution`の空repoを作る。各ディレクトリのmainを対応するrepoへpushしてから、workspace repoをpushする。`.gitmodules`の`../assurance`等はworkspaceのremoteと同じownerの兄弟repoへ解決される。別名・別ownerに配置する場合は`.gitmodules`を明示的に修正して`git submodule sync --recursive`を行う。

```sh
# 各コンポーネント内で、実際のownerに置き換える
git remote add origin git@github.com:OWNER/assurance.git
git push -u origin main
# 8つの子repo公開後、workspace直下でもoriginを設定してpushする
```

新規利用者は`git clone --recurse-submodules <workspace-url>`で取得する。既存cloneは`git submodule update --init --recursive`で固定版へ合わせる。`git submodule update --remote`は検証済みの組合せを変更するため、通常の取得手順には使わない。

CIはcommit SHAで固定したGitHub Actionsとchecksumで固定したproof toolchainを使う。native・proofの結果を別々に確認する。本番資格の未完条件はSTATUSに残し、native成功だけを根拠にrelease認定しない。

Debian配布物は[構築・記録・対応ソース収集の手順](../distribution/image/README.ja.md)に従う。Gitにはレシピと小さな検査記録を置き、ISO・DEB・対応ソースアーカイブは別の成果物保管先へ置く。公開前に実在する管理者連絡先、更新先、署名と保管責任、サポート範囲を設定する。現在は開発版であり、NiaOS独自の公開APT更新チャネルは提供していない。

現在の`0.1.0+git<commit>`は初期開発スナップショットの識別子であり、Git hashの大小をリリース順に使わない。公開更新ではコンポーネントのパッケージ版とintegrationのchangelogに増加する版を割り当て、生成済みDEBの新旧Versionを`dpkg --compare-versions NEW gt OLD`で確認する。同じ公開済み版へ異なる内容を上書きせず、新しい版としてビルド・受入・ソース保管を行う。[Debian PolicyのVersion規則](https://www.debian.org/doc/debian-policy/ch-controlfields.html#version)。
