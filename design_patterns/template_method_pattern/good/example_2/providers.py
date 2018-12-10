import os
import requests
import urllib.parse
from flask import redirect
from abc import ABCMeta, abstractmethod


class Provider(metaclass=ABCMeta):
    @abstractmethod
    def get_authorization_url(self): pass

    @abstractmethod
    def get_access_token_url(self): pass

    @abstractmethod
    def get_user_by_token(self, token): pass

    @abstractmethod
    def map_to_user(self, user): pass

    def authorize(self):
        return redirect(self.get_authorization_url())

    def user(self, code):
        token = self.request_access_token(code)
        user = self.get_user_by_token(token)
        return self.map_to_user(user)

    def request_access_token(self, code):
        request_params = {
            'code': code,
            'client_id': os.getenv('GITHUB_CLIENT_ID'),
            'client_secret': os.getenv('GITHUB_CLIENT_SECRET')
        }
        headers = {
            'Accept': 'application/json'
        }

        response = requests.post(self.get_access_token_url(), data=request_params, headers=headers)
        return response.json()['access_token']


class Github(Provider):
    def get_authorization_url(self):
        params = {
            'client_id': os.getenv('GITHUB_CLIENT_ID'),
            'redirect_uri': os.getenv('GITHUB_AUTHORIZATION_REDIRECT'),
            'scope': 'user:email'
        }

        return 'https://github.com/login/oauth/authorize?{}'.format(urllib.parse.urlencode(params))

    def get_access_token_url(self):
        return 'https://github.com/login/oauth/access_token'

    def get_user_by_token(self, token):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'token {}'.format(token)
        }

        response = requests.get('https://api.github.com/user', headers=headers)
        return response.json()

    def map_to_user(self, user):
        return {
            'username': user['login'],
            'name': user['name']
        }
