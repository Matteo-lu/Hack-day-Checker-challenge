#!/usr/bin/python3

import requests
from .get_token import intranet_hbn_get_token 
import intranet_hbn_scraper as scraper
from .intranet_hbn_scraper import intranet_hbn_scraper
import json

"""
[
    {
    "name": "name",
    "Tasks": 8,
    "checker": True
    }
]
"""

def is_true(list_t):
    """
    ...
    """

    true = 0
    false = 0

    for i in list_t:
        if i["checker_available"]:
            true += 1
        else:
            false += 1
    
    if true > false:
        return True
    else:
        return False


def get_dict(dict):
    """
    ...
    """

    new_dict = {}

    new_dict["name"] = dict["name"]
    new_dict["tasks"] = len(dict["tasks"])
    new_dict["checker"] = is_true(dict["tasks"])

    return new_dict


def get_info(user_email=None, password=None):
    """
    catch the users data
    """
    url = 'https://intranet.hbtn.io/'
    api_key = intranet_hbn_get_token(user_email, password)
    if api_key == None:
        return None
    print("api_key=" + api_key)
    url_token = "users/auth_token.json"

    parameters = {'api_key': api_key,
                  'email': user_email,
                  'password': password,
                  'scope': 'checker',}

    
    res = requests.post(url + url_token, data=parameters)
    auth_res = res.json()
    auth_token = auth_res["auth_token"]

    print("Auth token=" + auth_token)
    project_id = intranet_hbn_scraper(user_email, password)

    req = []
    for i in project_id:
        req.append(requests.get(url + 'projects/' + '{}.json?auth_token={}'.format(i, auth_token)).json())

    tasks = []
    
    for i in req:
        tasks.append(get_dict(i))

    return tasks

# https://intranet.hbtn.io/projects/434.json?auth_token=0123456789abcdef
