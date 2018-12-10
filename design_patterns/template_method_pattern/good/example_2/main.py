import os
from .providers import Github
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app.secret_key = os.getenv('APP_SECRET_KEY')


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
    user = github.user(code=request.args.get('code'))
    flash('Logged in as {} with user name {}'.format(user['name'], user['username']))
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
