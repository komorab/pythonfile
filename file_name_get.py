# 2022-2-12 用于读取文件夹内文件名并输出到指定文件
import os
import re

file_path = input('输入要读取的文件夹路径，如 D:\\PR\\Adobe，直接回车默认使用G:\n：')
name_path = input('输入要使用的文件名，直接回车默认name.doc\n：')
out_code = int(input('要添加序号输入1，不添加序号输入0，回车默认添加序号\n：'))
statue_code = int(input('读取所有文件名输入1， 读取歌曲名输入0\n：'))

if file_path == '':
    file_path = 'G:'
if name_path == '':
    name_path = 'name.txt'
out_path = file_path + '\\' + name_path

name = []
count = 0
files_list = os.listdir(file_path)
if statue_code == 0:
    for file_list in files_list:
        if re.search('《', file_list):
            count += 1
            half = file_list.split('《')
            fir = half[1]
            sec = fir.split('》')
            out = sec[0]
            if out_code == 0:
                name.append(out)
            else:
                name.append([count, out])
elif statue_code == 1:
    if out_code == 1:
        name = [[i+1, files_list[i]] for i in range(len(files_list))]
    elif out_code == 0:
        name = files_list[:]

with open(out_path, 'w') as f:
    for i in name:
        if out_code == 1:
            f.write(str(i[0])+' '+i[1]+'\n')
        else:
            f.write(i + '\n')
