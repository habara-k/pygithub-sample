import requests
from urllib.parse import parse_qs
from flask import Flask, request, redirect, session, url_for
from github import Github
from dotenv import dotenv_values


# .env ファイルから環境変数を取得する
# GITHUB_CLIENT_ID: https://github.com/settings/applications/new にアクセスして作る
# GITHUB_CLIENT_SECRET: 上に同じ
# FLASK_SECRET_KEY: flaskのsessionを使うためのシークレットーキー. 適当に設定すればいい.
env = dotenv_values(".env")

app = Flask(__name__)
app.secret_key = env["FLASK_SECRET_KEY"]


@app.route('/oauth')
def oauth():
    # あなたのGitHubアカウントをこのアプリに連携していいですか？の画面にリダイレクトする
    url = "https://github.com/login/oauth/authorize?client_id={}".format(env["GITHUB_CLIENT_ID"])
    return redirect(url)


@app.route("/callback/github")
def callback():
    # https://github.com/settings/applications/new のAuthorization callback URLで
    #   http://localhost:5000/callback/github を設定しておく
    # ユーザが連携を許可してくれたときに呼び出される

    # 入手したrequest.args['code']を利用してユーザのアクセストークンを発行する
    url = "https://github.com/login/oauth/access_token?code={}&client_id={}&client_secret={}".format(
        request.args['code'],
        env["GITHUB_CLIENT_ID"],
        env["GITHUB_CLIENT_SECRET"],
    )
    r = requests.get(url)
    access_token = parse_qs(r.text)['access_token'][0]

    # アクセストークンをsessionに保存し, 後から使えるようにする
    session['access_token'] = access_token
    return redirect(url_for('user'))


@app.route("/user")
def user():
    # sessionに保存してあるアクセストークンで PyGithubのGithubインスタンスを初期化する
    g = Github(session['access_token'])
    user = g.get_user()
    return "Hello, {}".format(user.name)
