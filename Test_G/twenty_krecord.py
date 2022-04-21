from re_video_download import DataRecord
import requests as r
import time
import json
import sys


url = 'https://api.bilibili.com/x/relation/stat?vmid=401315430'
uid = 401315430
file_path = 'G:/BVideo'


twe = DataRecord(uid, file_path, filename='twenty_krecord.json')
rec = twe.get_fans_num()
while 1:
    if twe.get_fans_num() != rec:
        print(twe.get_fans_num(), time.time(), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        rec = twe.get_fans_num()
    if twe.get_fans_num() == 200000:
        with open(f'{file_path}/{twe.filename}') as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        break
    time.sleep(1)
