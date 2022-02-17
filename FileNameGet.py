# 2022-2-16 编写一个类用于封装关于文件名搜索的函数

import re
import os


class FileNameGet:
    """
    获取指定文件夹的文件名称
    并以状态码决定是否要添加序号以及对文件名称和类型的筛选
    """

    def __init__(self,
                 file_path='G:',
                 file_name='name.txt',
                 out_code=1,
                 statue_code=0,
                 key_word=''):
        self.file_path = file_path
        self.file_name = file_name
        self.out_code = out_code
        self.statue_code = statue_code
        self.out_path = file_path + '\\' + file_name
        self.key_word = key_word

    def get_file(self) -> list:
        """获取文件名并添加序号"""
        return os.listdir(self.file_path)

# 这里应该先有一个函数用于处理或者筛选文件名（写俩函数吧
    def split_bracket(self, files_list: list) -> list:
        """处理文件名里面的书名号"""
        out_list = []
        for file_list in files_list:
            if re.search('《', file_list):
                half = file_list.split('《')
                fir = half[1]
                sec = fir.split('》')
                out = sec[0]
                out_list.append(out)
        return out_list

    def search_file(self, files_list: list) -> list:
        """根据关键词筛选文件名"""
        return [file_name
                for file_name in files_list
                if re.search(self.key_word, file_name)]

    def file_count(self, files_list: list) -> list:
        """给文件名添加序号"""
        return [str(files_list.index(file_name) + 1)+' '+file_name
                for file_name in files_list]

    def out_txt(self, files_list: list):
        """输出txt文件到指定文件夹"""
        with open(self.out_path, 'w') as f:
            for file_list in files_list:
                f.write(file_list + '\n')
            return 1


if __name__ == '__main__':
    do_file = FileNameGet()
    do_file.file_path = input('输入要读取的文件夹路径，如 D:\\PR\\Adobe，直接回车默认使用G:\n：')
    do_file.file_name = input('输入要使用的文件名，直接回车默认name.txt\n：')
    do_file.out_code = int(input('要添加序号输入1，不添加序号输入0，回车默认添加序号\n：'))
    do_file.statue_code = int(input('读取所有文件名输入1， 读取歌曲名输入0\n：'))
    do_file.key_word = input('输入筛选关键词，直接回车不进行关键词筛选\n：')
    ret_list = do_file.get_file()
    if do_file.statue_code == 0:
        ret_list = do_file.split_bracket(ret_list)
        if do_file.out_code == 1:
            ret_list = do_file.file_count(ret_list)
    elif do_file.statue_code == 1:
        if do_file.out_code == 1:
            ret_list = do_file.file_count(ret_list)
    do_file.out_txt(ret_list)
