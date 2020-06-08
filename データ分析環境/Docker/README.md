# Docker
Docker環境上でjupyterを起動する方法をまとめました。

Dockerfile.jupyter
```
FROM jupyter/datascience-notebook
MAINTAINER gtaiyou24

USER root

# matplotlib日本語化
RUN curl -L "https://ipafont.ipa.go.jp/IPAexfont/ipaexg00301.zip" > font.zip \
    && unzip font.zip \
    && cp ipaexg00301/ipaexg.ttf /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/ipaexg.ttf \
    && echo "font.family : IPAexGothic" >>  /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc \
    && rm -r ./.cache

# 作業ディレクトリに移動
WORKDIR /home/jovyan/work
```
```bash
$ docker build -t ml-jupyter:latest Dockerfile.jupyter
$ docker image ls 
$ docker container run --rm \
    -e GRANT_SUDO=yes \
    -e NB_UID=$UID \
    -e NB_GID=$GID \
    -e TZ=Asia/Tokyo \
    -p 8888:8888 \
    --name notebook \
    -v ~/path/to/directory/:/home/jovyan/work \
    ml-jupyter:latest start-notebook.sh --NotebookApp.password=''
```

## 参考文献

 - [jupyter/datascience-notebook - Docker Hub](https://hub.docker.com/r/jupyter/datascience-notebook/)
 - [Dockerで構築するJupyter notebookのデータ分析環境 | ぱーくん plus idea](https://web.plus-idea.net/on/docker-jupyter-notebook-python/)
 - [Dockerで基本的なData Science環境(Jupyter, Python, R, Julia, 定番ライブラリ)を構築する。 - Qiita](https://qiita.com/y4m3/items/c2703d4e131e05084b7b)