# Guide

1. Pythonの仮想環境を作る
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. https://github.com/settings/applications/new でOAuthアプリケーションを登録.
Authorization callback URLは http://localhost:5000/callback/github に設定すること.

3. .env ファイルを作る.

```
GITHUB_CLIENT_ID={1.で作成したClient ID}
GITHUB_CLIENT_SECRET={1.で作成したClient secrets}
FLASK_SECRET_KEY={適当な値}
```

4. バックエンドを起動
```
export FLASK_ENV=development
export FLASK_APP=hello
flask run
```

5. 別タブを開いてフロントエンドを起動. 
```
source venv/bin/activate
python -m http.server 8080
```

6. http://localhost:8080/ にアクセス
7. Sign in With Github をクリックし, Authorizeする
8. http://localhost:8080/user にリダイレクトされて, Githubのユーザ名が表示されてたらOK
