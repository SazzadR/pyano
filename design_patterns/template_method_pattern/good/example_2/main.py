import os
from .providers import Github
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/auth/redirect/github')
def authorize_github():
    github = Github()
    return github.authorize()


@app.route('/auth/callback/github')
def login():
    github = Github()
    github.user(code=request.args.get('code'))
    return 'abc'


if __name__ == '__main__':
    app.run(debug=True)
