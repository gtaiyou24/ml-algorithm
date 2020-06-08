# ML
機械学習/統計分析パッケージ

## jupyterの起動方法
```bash
$ docker build -t ml-jupyter:latest .
$ docker image inspect ml-jupyter:latest
$ docker container run --rm \
    -e GRANT_SUDO=yes \
    -e NB_UID=$UID \
    -e NB_GID=$GID \
    -p 8888:8888 \
    --name ml-jupyter \
    -v `pwd`:/home/jovyan/work \
    ml-jupyter:latest start-notebook.sh --NotebookApp.password=''
```

---
## データセット

 - HR_comma_sep.csv: download from [Human Resources Analytics | Kaggle](https://www.kaggle.com/ludobenistant/hr-analytics)

---
## jupyter notebookをPDFで保存する方法
ブラウザでnotebookを開き、extension機能のページ目次を閉じて、Command+Pで保存される。