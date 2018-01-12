# 一般化線形モデル(1章 序論)
## 範囲


## 表記法

 - 確率変数: $Y_{1}, Y_{2}, \dots, Y_{n}$
 - 観測値: $y_{1}, y_{2}, \dots, y_{n}$
 - パラメータ(母数): $\beta$
 - 推定量: $\widehat {\beta}$

連続的な確率変数**$Y$**の確率密度関数(または$Y$が離散的なときの確率関数)
$$
f\left( y;\theta \right)
$$
ここに**$\theta$**は分布のパラメータである。

和を表すためにドット($.$)、平均を表すためにバーを用い
$$
\bar {y} = \frac {1}{N} \sum _{i=1}^{N}{y_{i}} = \frac {1}{N} y.
$$
のように使用する。

確率変数$Y$の期待値と分散

 - $E\left(Y\right)$
 - $var\left(Y\right)$

たとえば、確率変数$Y_{1}, \dots, Y_{n}$が独立で、$E\left(Y_{i}\right) = \mu_{i}$、$var\left(Y_{i}\right) = {\sigma_{i}}^{2}$,確率変数$W$が$Y_{1}, \dots, Y_{n}$の**線形結合**(linear combination)で以下のように表せるとする。

$$
W = a_{1}Y_{1} + a_{2}Y_{2} + \cdots + a_{n}Y_{n} \qquad (1.1)
$$
ただし、$a_{1}, \cdots, a_{n}$は定数である。このとき$W$の期待値は
$$
E\left(W\right) = a_{1}\mu_{1} + a_{2}\mu_{2} + \cdots + a_{n}\mu_{n} \qquad (1.2)
$$
と表され、その分散は
$$
var\left(W\right) = {a_{1}}^{2}{\sigma_{1}}^{2} + {a_{2}}^{2}{\sigma_{2}}^{2} + \cdots + {a_{n}}^{2}{\sigma_{n}}^{2} \qquad (1.3)
$$
と表される。
