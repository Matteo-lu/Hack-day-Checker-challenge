#!/usr/bin/python3

import requests
from getpass import getpass
from api import get_token

def get_info(user_email=None, password=None):
    """
    .....
    """
    url = 'https://intranet.hbtn.io/'
    api_key = get_token.intranet_hbn_scraper(user_email, password)
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


project_id = input("Enter id project ")
project_req = requests.get(url + 'projects/' + project_id)