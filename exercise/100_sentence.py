# 23-5-10 to send 100 message
import time
from pynput import keyboard, mouse


def main():
    my_mouse = mouse.Controller()  # 创建鼠标
    my_keyboard = keyboard.Controller()  # 创建键盘
    x_position = 850
    y_position = 750
    my_mouse.position = (x_position, y_position)
    my_mouse.click(mouse.Button.left)
    for i in range(100):
        my_keyboard.type(f'message{i}')
        my_keyboard.press(keyboard.Key.enter)  # 按回车enter
        my_keyboard.release(keyboard.Key.enter)  # 松开回车enter
        time.sleep(0.2)

if __name__ == '__main__':
    time.sleep(10)
    main()