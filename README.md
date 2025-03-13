# Densha Bot API

## 介紹

本プロジェクトは、Yahoo運行情報サイトから情報をクロールし、電車/私鉄/地下鉄など、様々な路線の遅延情報を取得するAPIです。
このAPIを利用することで、現在の路線の遅延情報を簡単に取得でき、これを利用した各種アプリの開発が可能です。

## URL

## 設置
1. 必要なパッケージをインストール：
```bash
pip install -r requirements.txt
```
2. env.example ファイルを編集し、設定を入力する：
```bash
cp .env.example .env
vi .env.example
```
```bash
MYSQL_HOST=localhost
MYSQL_DATABASE=densha_bot_api
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_PORT=3306
```

3. データベースを準備する：
```bash
python manage.py migrate
```

4. 起動する：
python manage.py runserver

## 使用方法

### `GET /densha/routes/`
すべての路線の最新情報を取得する。

#### クエリオプション (Query):
- `offset` : 別のページの情報を取得するためのオフセット。  
  **例:** `/densha/routes/?offset=10`

- `search` : 指定した路線を検索するためのクエリ。  
  **例:** `/densha/routes/?search=山手線`


## Issues
このプロジェクトに問題がある場合や新機能の要望があれば、気軽にIssueまたはPull Requestを作成してください。
