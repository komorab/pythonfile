# 23-5-10 定时自动发消息脚本

import os
import time
from pynput import keyboard, mouse

std_time = 1683651752  # 2023-05-10 01:02:32
day_sec = 24 * 3600
count = 25

message = ["晚安"]

my_mouse = mouse.Controller()  # 创建鼠标
my_keyboard = keyboard.Controller()  # 创建键盘
x_position = 850
y_position = 750


def main():
    while True:
        if time.time() > (std_time + day_sec * count + 600):

            my_mouse.position = (x_position, y_position)
            my_mouse.click(mouse.Button.left)
            for i in message:
                my_keyboard.type(i)
                my_keyboard.press(keyboard.Key.enter)  # 按回车enter
                my_keyboard.release(keyboard.Key.enter)  # 松开回车enter
                time.sleep(1)

            os.system('shutdown -s -t 10')
            break
        time.sleep(600)
        with open("D:\\PycharmProject\\pythonfile\\exercise\\MessageLog", "a") as f:
            f.write(f'{my_mouse.position}  {(std_time + day_sec * count + 600) - time.time():.4f}  {time.time():.4f}\n')


def positionTest():
    my_mouse.position = (x_position, y_position)


if __name__ == '__main__':
    main()
    # positionTest()
