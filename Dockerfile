FROM ubuntu:24.04
USER root
COPY . /app
WORKDIR /app
# apt-getの速度を向上させる
RUN sed -i 's@ports.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y python3-pip

# VENVのインストール
RUN apt-get install -y python3-venv
RUN python3 -m venv .venv

SHELL ["/bin/bash", "-c", "source .venv/bin/activate"]
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN setcap 'cap_net_bind_service=+ep' /usr/local/bin/gunicorn
RUN mkdir -p /var/log/gunicorn/
