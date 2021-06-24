# Guide

1. https://github.com/settings/applications/new でOAuthアプリケーションを登録.
Authorization callback URLは http://localhost:5000/callback/github に設定すること.

2. .env ファイルを作る.

```
GITHUB_CLIENT_ID={1.で作成したClient ID}
GITHUB_CLIENT_SECRET={1.で作成したClient secrets}
FLASK_SECRET_KEY={適当な値}
```

3. バックエンドを起動
```
export FLASK_ENV=development
export FLASK_APP=hello
flask run
```

4. フロントエンドを起動
```
python -m SimpleHTTPServer 8080
```

5. http://localhost:8080/ にアクセス
6. Sign in With Github をクリックし, Autorizeする
7. http://localhost:8080/user にリダイレクトされて, Githubのユーザ名が表示されてたらOK