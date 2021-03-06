# データ解析テンプレート

## 初期設定
```bash
pip install cookiecutter

cookiecutter https://github.com/drivendata/cookiecutter-data-science.git
```

 - https://qiita.com/Hironsan/items/4479bdb13458249347a1
 - https://github.com/drivendata/cookiecutter-data-science
 - http://univprof.com/archives/16-02-11-2849465.html
 - http://univprof.com/archives/16-05-01-2850729.html

## データ解析のフロー

 1. **目的設定**
 	- 仮説検証型アプローチ : あらかじめなんらかの仮説があり、データによってその仮説を検証するアプローチ
 	- 探索的アプローチ : データから目的を生み出すためのアプローチ
 2. **分析計画**
 	- 評価指標と達成基準の設定 : データ分析に直結する指標が必要
 	- 成果物の設定 : ①対象者のレベルに合っているか②ニーズに合っているか を確認しながら最終的な成果物を決めます.
 	- MoSCow分析(整理) : この段階で取り組みたい案が数多くあるが、リソースが足らない場合はタスクの優先度をつける
 		- 「必須で行わなければならないMustな要件」
 		- 「できる限り行うべきShouldな要件」
 		- 「もし余力があって可能ならば行ってもよいCouldな案件」
 		- 「行わないWon'tな案件」
 3. **データ設計**
 4. **データ収集・保存**
 5. **データの前処理**
 6. **分析手法選択と適用**
 7. **分析結果の解釈**
 8. **施策の提案** : 実現性がある適切な提案を行うために、提案時に伝えるべき内容は以下のようなものがあります
 	- 目的 : 最終的に達成すべきこと. １つでも複数でもよい.
 	- 仮説 : データ解析を進める際の出発点
 	- 事実
 	- 解釈
 	- 予測
 	- 提案
 	- 例
 9. **実施と検証**
 10. **反省,さらなる改善のために...**