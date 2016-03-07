# -*- coding: utf-8 -*-

import requests
import time
import json
import os

image_locate = '/Volumes/tfstore/picture'
bing_wallpapers_url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8'
clean_dumplicate = 'rm /Volumes/tfstore/picture/*.[0-9]'

cmd_save_photo = 'wget %s -P %s'

s = requests.session()

result = s.get(bing_wallpapers_url).text
json = json.loads(result)
images = json['images']
for image in images:
    image_url = image['url']
    os.system(cmd_save_photo % (image_url,image_locate))
os.system(clean_dumplicate)

