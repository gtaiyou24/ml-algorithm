# MeCab

## MeCabのインストール方法
環境はmac.

### HomebrewでMeCabと辞書をインストール
```bash
brew install mecab
brew install mecab-ipadic
```

### gccのインストール
```bash
brew install gcc
ln -s /usr/local/bin/gcc-8 /usr/local/bin/gcc
ln -s /usr/local/bin/g++-8 /usr/local/bin/g++
```
.bash_profile なり .zshrc なりを編集して、`which gcc`が`/usr/local/bin/gcc`となるようにする。


### mecab-ipadic-NEologdをインストール
これはWeb上の新語をデフォルトの辞書に追加したもの

**標準設定(一部の辞書はインストールされない)**
```bash
brew install git curl xz
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n
```

**全辞書をインストールする場合**<br>
```bash
brew install git curl xz
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n -a
```

### mecab-python3をインストール
```bash
brew install swig
pip install mecab-python3
```

### `MeCab.Tagger`のパス
MeCab.Taggerで指定するパスは以下の結果
```bash
echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
```

### 実行
```python
import MeCab

m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
print(m.parse("コーヒー牛乳とラーメン"))
# コーヒー牛乳    名詞,固有名詞,一般,*,*,*,コーヒー牛乳,コーヒーギュウニュウ,コーヒーギュウニュー
# と 助詞,並立助詞,*,*,*,*,と,ト,ト
# ラーメン  名詞,一般,*,*,*,*,ラーメン,ラーメン,ラーメン
# EOS
```
