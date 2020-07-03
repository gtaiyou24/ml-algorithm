# Docker

## Dockerfile.gpu
GPU環境対応のDockerfileです。このDockerfileは以下の前提条件があります。

　- [Dockerfile.gpu](./Dockerfile.gpu) と同階層に`requirements.txt`を作成してあること

```bash
$ docker build -t ml-gpu:latest Dockerfile.gpu
$ docker image ls | grep ml-gpu
$ 
```

## Dockerfile.jupyter
jupyterを起動するDockerfileです。このDockerfileは以下の前提条件があります。

 - [Dockerfile.jupyter](./Dockerfile.jupyter) と同階層に`requirements.txt`を作成してあること

```bash
$ docker build -t ml-jupyter:latest Dockerfile.jupyter
$ docker image ls | grep ml-jupyter
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