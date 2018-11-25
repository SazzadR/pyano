import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/authorize')
def authorize():
    client_id = 'd181717538f92576b383'
    client_secret = '1e7fa177d06e004cd3d81520af862b8b3e17915b'
    authorization_url = 'https://github.com/login/oauth/authorize?client_id={}'.format(client_id)
    return redirect(authorization_url)


@app.route('/github/login')
def login():
    code = request.args.get('code')
    client_id = 'd181717538f92576b383'
    client_secret = '1e7fa177d06e004cd3d81520af862b8b3e17915b'
    request_body = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret
    }
    print(request_body)
    return 'a'


if __name__ == '__main__':
    app.run(debug=True)
