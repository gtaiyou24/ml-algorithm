# 一般化線形モデル(1章 序論)

<table>
    <tr>
        <th rowspan="2">名義尺度</th>
        <td>2値変数</td>
        <td>男/女, 死亡/生存</td>
    </tr>
    <tr>
        <td>多項変数</td>
        <td>赤/緑/青</td>
    </tr>
    <tr>
        <th>順序尺度</th>
        <td>-</td>
        <td>若年/中年/老年 (カテゴリー間に何らかの自然順序のある変数)</td>
    </tr>
    <tr>
        <th>連続尺度</th>
        <td>間隔尺度/比尺度</td>
        <td>重さ、長さ、時間</td>
    </tr>
</table>

<table>
    <tr>
        <th>反応変数(結果変数,従属変数)</th>
        <th>説明変数(独立変数)</th>
        <th>手法</th>
    </tr>
    <tr>
        <td rowspan="4">連続変数</td>
        <td>2値</td>
        <td>t検定</td>
    </tr>
    <tr>
        <td>名義,3つ以上のカテゴリー, 順序</td>
        <td>分散分析</td>
    </tr>
    <tr>
        <td>名義と小数個の連続</td>
        <td>共分散</td>
    </tr>
    <tr>
        <td>連続,カテゴリー</td>
        <td>重回帰</td>
    </tr>
    <tr>
        <td rowspan="3">2値</td>
        <td>カテゴリー</td>
        <td>分割表/ロジスティック回帰</td>
    </tr>
    <tr>
        <td>連続</td>
        <td>ロジスティック,プロビットなどの用量反応モデル</td>
    </tr>
    <tr>
        <td>カテゴリーと連続</td>
        <td>ロジスティック回帰</td>
    </tr>
    <tr>
        <td rowspan="2">3カテゴリー以上の名義</td>
        <td>名義</td>
        <td>分割表</td>
    </tr>
    <tr>
        <td>カテゴリーと連続</td>
        <td>名義ロジスティック回帰</td>
    </tr>
    <tr>
        <td>順序</td>
        <td>カテゴリーと連続</td>
        <td>順序ロジスティック回帰</td>
    </tr>
    <tr>
        <td rowspan="2">計数または度数</td>
        <td>カテゴリー</td>
        <td>対数線形モデル</td>
    </tr>
    <tr>
        <td>カテゴリーと連続</td>
        <td>ポアソン回帰</td>
    </tr>
    <tr>
        <td>故障時間</td>
        <td>カテゴリーと連続</td>
        <td>生存時間解析</td>
    </tr>
    <tr>
        <td>相関のある反応</td>
        <td>カテゴリーと連続</td>
        <td>一般化推定方程式,多段階モデル</td>
    </tr>
</table>

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
