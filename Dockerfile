# Ubuntuベースイメージを使用
FROM ubuntu:20.04

# インストールとアップデート
RUN apt-get update && apt-get install -y tzdata
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip
RUN apt-get clean
RUN pip3 install --upgrade pip
RUN  pip3 install --upgrade pip setuptools 
RUN apt-get install -y libpq-dev
RUN  pip3 install python-dotenv
RUN apt-get install -y vim
WORKDIR /src


COPY ./ /src

# 必要なPythonライブラリをインストール
RUN pip3 install -r /src/requirements.txt
EXPOSE 3031