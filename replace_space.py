def replace_space():
    'to replace the space of a string'
    s = input('input the string: ')
    s.replace(' ','')
    print(s)
    return s
#问题：input接受的字符有空格会分为几个字符串
#能不能以输入几个就记录几个，然后再合并


if __name__ == '__main__':
    print(replace_space())