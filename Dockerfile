FROM jupyter/datascience-notebook
MAINTAINER gtaiyou24

USER root

ENV TZ=Asia/Tokyo

# matplotlib日本語化
RUN curl -L "https://ipafont.ipa.go.jp/IPAexfont/ipaexg00301.zip" > font.zip \
    && unzip font.zip \
    && cp ipaexg00301/ipaexg.ttf /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/ipaexg.ttf \
    && echo "font.family : IPAexGothic" >>  /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc \
    && rm -r ./.cache

WORKDIR /home/jovyan/work