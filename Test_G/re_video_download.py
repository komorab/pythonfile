# 用于记录数据的变化，不过现在的手段还是太粗糙了，尽量写一个class让main更少
# 2022-2-11 如果把数据和dict加入self，每次调用self时不会刷新，不过勉强可以用了
import sys
import time
import requests as r
import json


class DataRecord:
    def __init__(self, uid: int, filepath=sys.path[0], filename='FollowerRecord.json'):
        self.uid = uid
        self.url = f'https://api.bilibili.com/x/relation/stat?vmid={uid}'
        if filepath == sys.path[0]:
            self.filepath = filepath + filename
        else:
            self.filepath = filepath

    def get_fans_num(self) -> int:
        """从get到的json数据中获取follower数据"""
        response = r.get(self.url)
        if response.status_code == 200:
            # 判断get状态是否正常
            responses_dict = response.json()
            response_dict = responses_dict['data']
            num = response_dict['follower']
            return num

    def record_dict(self, statue=1) -> dict:
        """
        将时间-数量转化为key-value形式并成为一个dict并入和返回整个数据dict
        statue用于输出指定数据：
            1：follower（好像没几个能够输出
        """
        record = {}
        if statue == 1:
            record.clear()
            record[time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())] = DataRecord.get_fans_num(self)
        return record

    def write_num(self):
        """文件不存在时会报错，下次修复"""
        with open(self.filepath, 'r') as read:
            list_record = list(json.load(read))
            list_record.append(DataRecord.record_dict(self))
        with open(self.filepath, 'w') as file:
            json.dump(list_record, file, indent=4)


bili_url = 'https://api.bilibili.com/x/relation/stat?vmid=401315430'
bili_uid = 401315430

'''{'code': 0, 'message': '0', 'ttl': 1,
'data': {'mid': 401315430, 'following': 20, 'whisper': 0, 'black': 0, 
'follower': 160679}} '''

file_path = 'D:/BVideoFiles/22886883-星瞳_Official/record_fans_num.json'


if __name__ == '__main__':
    count = 1
    Data_Record = DataRecord(bili_uid, filepath=file_path)
    while 1:
        c_time = time.strftime('%H:%M:%S', time.localtime())

        if count:
            if c_time[6:8] == '00':
                count -= 1
        else:
            Data_Record.write_num()
            time.sleep(600)
