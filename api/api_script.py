#!/usr/bin/python3

import requests
from getpass import getpass
from api import get_token

url = 'https://intranet.hbtn.io/users/auth_token.json'
api_key = get_token.intranet_hbn_scraper("2809@holbertonschool.com", "Julioc8172315")
user_email = input("Your Holberton email")
password = getpass("Your intranet password")
url_token = "users/auth_token.json"

parameters = {'api_key': api_key,
              'email': user_email,
              'password': password,
              'scope': 'checker',}

try:
    auth_res = requests.post(url + url_token, data=parameters)
    auth_token = auth_res['auth_token']
except:
    pass
