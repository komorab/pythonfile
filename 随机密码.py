#2020-4-24
#用于随机生成一个六位数或者四位数的密码

import time
import random

if __name__ == '__main__':
    weishu = int(input('输入数字生成相应位数随机数字：'))
    if isinstance(weishu, int):
        for i in range(0, weishu):
            print(random.randint(0,9), end='')
    else:
        print('输入有误，请重新启动')
    print('\n')
    print('30秒后退出')
    time.sleep(30)