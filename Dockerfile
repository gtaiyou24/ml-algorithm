FROM jupyter/datascience-notebook
MAINTAINER gtaiyou24

USER root

ENV TZ=Asia/Tokyo

# matplotlib日本語化
RUN curl -L "https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00401.zip" > font.zip \
    && unzip font.zip \
    && cp IPAexfont00401/ipaexg.ttf /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/ipaexg.ttf \
    && echo "font.family : IPAexGothic" >>  /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc \
    && rm -r ./.cache

WORKDIR /home/jovyan/work