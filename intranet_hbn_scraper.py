#!/usr/bin/python3
"""module containing the function intranet_hbn_scraper"""


def intranet_hbn_scraper(user_mail, user_paswd):
    """Function that enters the home page of holberton and
    extracts the id of the current projects"""
    import requests
    import bs4
    from bs4 import BeautifulSoup
    from os import system
    from sys import argv

    SIGN_IN_URL = 'https://intranet.hbtn.io/auth/sign_in'
    home_URL = 'https://intranet.hbtn.io'

    # run a new requests session
    with requests.Session() as s:
        # get the response object
        print('Accesing the intranet:...')
        intranet_response = s.get(SIGN_IN_URL)
        print('Established connection with status code: {}\n'.format(
            intranet_response.status_code))

    # pull LOG-IN html data with BeautifulSoup
    soup = BeautifulSoup(intranet_response.text, 'html.parser')
    # get the authenticity_token
    key = soup.find('input', {'name': 'authenticity_token'}).get('value')

    payload = {
        'user[login]': user_mail,
        'user[password]': user_paswd,
        'authenticity_token': key,
        'user[remember_me]': '1',
        'commit': 'submit'
    }
    # send payload by post method
    send_login = s.post(SIGN_IN_URL, data=payload)

    project_response = s.get(home_URL)

    # pull PROJECT html data
    soup = BeautifulSoup(project_response.text, 'html.parser')

    projects_codes = []
    for li in soup.main.article.ul:
        if isinstance(li, bs4.element.Tag):
            projects_codes.append(li.code.text)

    print(projects_codes)

# intranet_hbn_scraper("2640@holbertonschool.com", "Mlu001937465123")
