# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import json
import glob


class Login(object):
    def __init__(self, url_login="https://atcoder.jp/login?"):
        self.session = requests.session()
        self.url_login = url_login

    def set_login_info(self):
        info_file = glob.glob("../login_info/*.json")[0]
        with open(info_file) as f:
            self.login_info = json.load(f)

    def login(self):
        r = self.session.get(self.url_login)
        s = BeautifulSoup(r.text, 'html5lib')
        csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')
        self.set_login_info()
        self.login_info["csrf_token"] = csrf_token
        result = self.session.post(self.url_login, data=self.login_info)
        result.raise_for_status()
        if result.status_code == 200:
            print("log in!")
        else:
            print("failed")
