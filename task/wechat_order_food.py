# -*- coding: utf-8 -*-

import requests
import sys
import codecs
import time
user_name = '0078'
pswd = 'mark410521'
url_login = "http://wcent.duitang.net/napi/login/checkpwd/"
url_order = "http://wcent.duitang.net/napi/backend/dinner/book/"

name_list = ['可可','小易']

s = requests.session()

postdata = {
	'loginname': user_name,
	'password': pswd
}
r1 = s.post(url_login, postdata)
postdata1 = {
   'count': 1,
   'memo': '可可',
   'platform': 'WEB'
}

for name in name_list:
    postdata1['memo'] = name
    r2 = s.post(url_order,postdata1)
    print r2.text
