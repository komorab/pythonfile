import time
import requests as r
import json


class DataRecord:
    def __init__(self, url: str, filename: str, record={}):
        self.url = url
        self.record = record
        self.filename = filename
        self.record_fin = DataRecord.fans_record_dict(self)

    def get_num(self):
        """get the number of uid or follower or following"""
        response = r.get(self.url)
        if response.status_code == 200:
            responses_dict = response.json()
            response_dict = responses_dict['data']
            num = response_dict['follower']
            return num

    def fans_record_dict(self):
        """record the number of fans as a dictionary"""
        record_fin = {}
        self.record = {}
        self.record[time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())] = DataRecord.get_num(self)
        # 调用之后record不会清空
        for rec in self.record:
            record_fin[rec] = self.record[rec]
        return record_fin

    def write_num(self):
        with open(self.filename, 'a+') as file:
            json.dump(self.record_fin, file, indent=4)


bili_url = 'https://api.bilibili.com/x/relation/stat?vmid=401315430'

'''{'code': 0, 'message': '0', 'ttl': 1,
'data': {'mid': 401315430, 'following': 20, 'whisper': 0, 'black': 0, 
'follower': 160679}} '''

file_path = 'D:/BVideoFiles/22886883-星瞳_Official/record_fans_num.json'


if __name__ == '__main__':
    count = 1
    Data_Record = DataRecord(bili_url, file_path)
    while 1:
        c_time = time.strftime('%H:%M:%S', time.localtime())

        if count:
            if c_time[6:8] == '00':
                count -= 1
        else:
            with open(file_path, 'r') as f:
                data_load = list(json.load(f))
                data_load.append(Data_Record.fans_record_dict())

            with open(file_path, 'w') as fin:
                json.dump(data_load, fin, indent=4)
            time.sleep(600)
