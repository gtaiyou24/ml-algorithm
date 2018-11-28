# バンディットアルゴリズム(Bandit Algorithms)
## バンディット問題とは
> いま、あなたはスロットマシンで一儲けしようとカジノに来ているとする。
>
> - アームが1本ずつ付いたスロットマシンが $K=5$ 台ある
> - たまたま客は自分以外誰もおらず5つのアームのどれでも引ける
> - どのアームが当たりやすいのかに関し、はじめは何の情報もない
>
> 1回ごとにアームを選んで合計100回引く場合、各回に引くアームをあなたはどのように選択するか？

あなたは、5つのアームのうち最も当たりやすいアームを引きたいと考えるが、３つ目の仮定よりはじめは当たりやすいアームがわからない。
そのため、各アームを$n$回ずつ引いて、1番当たりの多かったアームを残りの$(100 - 5n)$回引くことにした。

**<font color="red">$n$の値をどうやって設定する？</font>**

 - $n$ の値を小さい値に設定: ex)各アームを3回ずつ引いて1番当たりの多かったアームを残り85回引くとする→たった3回引いただけで1番当たりやすいアームを見極めるのは難しい
 - $n$ の値を大きな値に設定: ex)各アームを15回ずつ引いて1番当たりの多いアームを残りの15回引くとする→残りたったの15回では最も当たりやすいアームであっても大きな儲けを得ることはできない


この問題では、あるアームが当たりやすいか否かという情報は、実際にそのアームを引いた結果のみから得られる。

情報の少ないアームを選ぶ**<font color="blue">探索</font>**(exploration)&それまでに最も当たりの多かったアームを引く**<font color="blue">知識利用</font>**(exploitation)を行う。

この探索と知識利用のバランスをどうすればよいかという問題は、**<font color="blue">探索と知識利用のトレードオフ</font>**(exploration-exploitation trade-off)として知られる。

> ### バンディット問題(bandit problem)
> 選択肢の集合から1つの要素を選択し、その選択肢にしたする報酬を得るがほかの選択肢の報酬情報は得られない、というプロセスを繰り返す設定において、報酬和の最大化を目指す逐次決定問題

| 用語 | 説明 |
|:----|:-----|
| **多腕バンディット**<br>(multi-armed bandit problem) | $K$台のスロットマシンから1台のスロットマシンを選んでアームを引くことを繰り返して<br>儲けの最大化を目指す問題 |
| **アーム**(arm) | 選択肢 |
| **方策**(policy) | プレイヤーがそれまでに得た報酬をもとに次に引くアームを決定する戦略のこと |

## 確率的バンディットと敵対的バンディット

| 種類 | 説明 |
|:-----|:----|
| **確率的バンディット**(stochastic bandit) | 各アームからの報酬が何らかの確率分布に従って生成される |
| **敵対的バンディット**(adversarial bandit) | プレイヤーの方策を知っている敵対者が報酬を決める場合を想定する |


## プレイヤー方策の評価法

 - $X_{i}\left(t\right)$ : アーム$i$の時刻$t$における報酬
 - $i\left(t\right)$: 時刻$t$にプレイヤーが選ぶアーム

プレイヤーの目標としては主に以下の2つの量のいずれかの最大化を目指す問題が考えられる。

#### 1. 有限時間区間(finite horizon)における累積報酬(cumulative reword)
$$
\sum _{t=1}^{T}{X_{i\left(t\right)}\left(t\right)}
$$

#### 2. 無限時間区間(infinite horizon)における幾何割引(geometric discount)された累積報酬
$$
\sum _{t=1}^{\infty}{ { \gamma  }^{ t-1 }{ X }_{ i\left( t \right)  }\left( t \right)  }
$$

最近では、有限時間区間における累積報酬で方策を評価するのが主流

プレイヤーの目的は、これらの累積報酬を最大化する**方策を構成すること**だが、このような累積報酬の大小は、

 - 方策の良し悪し= $i\left(t\right)$がよかったか
 - 報酬の組み合わせ $\left\{ X_{i}\left(t\right) \right\}_{i,t}$ が全体として大きめだったか = $X_{i}\left(t\right)$がよかったか

に依存する。そこで純粋な方策のよさを評価するために、(何らかの意味で)最適な方策をとった場合の累積報酬を目標値とし、それとの差を比較するということが通常行われる。

ここで到達し得る累積報酬の最大値は
$$
\sum _{t=1}^{T}{ \max _{i \in \left\{1,\cdots,K \right\}}{ X_{i}\left(t\right) } }
$$
ですが、これは目標として高すぎるので、同じ選択を選び続けた場合の累積報酬の最大値
$$
\max _{ i\in \left\{ 1,\cdots ,K \right\}  }{ \sum _{ t=1 }^{ T }{ { X }_{ i }\left( t \right)  }  }
$$
を目標とする。

この目標値と、プレイヤーの累積報酬$\sum _{t=1}^{T}{X_{i\left(t\right)}\left(t\right)}$との差
$$
Regret\left( T \right) =\max _{ i\in \left\{ 1,\cdots ,K \right\}  }{ \sum _{ t=1 }^{ T }{ { X }_{ i }\left( t \right)  }  } -\sum _{ t=1 }^{ T }{ { X }_{ i\left( t \right) }\left( t \right)  } \qquad (1.1)
$$
を**リグレット**とよび、この値の最小化を目指す。リグレットは、プレイヤーが「あの方策をとっておけばよかったのに...」という後悔(regret)の大きさを表している値と考えられる。

各時刻$t$におけるプレイヤー方策の選択$i\left(t\right)$も報酬$X_{i}\left(t\right)$も確率的な場合を扱うことが多いので、リグレットよりも**期待リグレット**(expected regret)
$$
E\left[ Regret\left( T \right)  \right] =E\left[ \max _{ i\in \left\{ 1,\cdots ,K \right\}  }{ \sum _{ t=1 }^{ T }{ { X }_{ i }\left( t \right)  }  } -\sum _{ t=1 }^{ T }{ { X }_{ i\left( t \right)  }\left( t \right)  }  \right] \qquad (1.2)
$$
さらに**擬リグレット**(pseudo-regret)
$$
\overline { Regret } \left( T \right) =\max _{ i\in \left\{ 1,\cdots ,K \right\}  }{ E\left[ \sum _{ t=1 }^{ T }{ { X }_{ i }\left( t \right)  } -\sum _{ t=1 }^{ T }{ { X }_{ i\left( t \right)  }\left( t \right)  }  \right]  } \qquad (1.3)
$$
を用いた評価がよく行われる。ここで、擬リグレットは期待リグレット以下の値をとる。つまり
$$
\overline {Regret}\left(T\right) \le E\left[ Regret\left(T\right) \right]
$$
が常に成り立つ。


---
# 参考文献

 - [バンディットアルゴリズム　基本編 | ALBERT Official Blog](https://blog.albert2005.co.jp/2017/01/23/%E3%83%90%E3%83%B3%E3%83%87%E3%82%A3%E3%83%83%E3%83%88%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%80%80%E5%9F%BA%E6%9C%AC%E7%B7%A8/)
 - [A/Bテストよりすごい？バンディットアルゴリズムとは一体何者か - Qiita](https://qiita.com/yuku_t/items/6844aac6008911401b19)
 - [バンディットアルゴリズム入門と実践 - SlideShare](https://www.slideshare.net/greenmidori83/ss-28443892)
 - [A/Bテストより無駄なく最適化できる？バンディットアルゴリズムを試してみた / PLAID Engineer  Blog](https://tech.plaid.co.jp/banditalgorithms/)
 - [バンディットアルゴリズムの評価と因果推論 | Research Blog](https://adtech.cyberagent.io/research/archives/199)
 - [Pythonでバンディットアルゴリズム](https://eng.iridge.jp/post/2014/bandit-with-python/)
 - [多腕バンディット問題: 定式化と応用 (第13回ステアラボ人工知能セミナー) - SlideShare](https://www.slideshare.net/stairlab/13-80135631)
