# 23-5-10 获取鼠标点击的坐标


import time,os
import pyautogui as pag

def main():
	try:
		while True:
			print('点击 Ctrl-C 结束')
			# 获取屏幕的尺寸
			screenWidth, screenHeight = pag.size()
			x, y = pag.position()
			#返回鼠标的坐标
			# print('屏幕尺寸: (%s %s),  鼠标坐标 : (%s, %s)' % (screenWidth, screenHeight, x, y))
			print(f'ScreenSize: ({screenWidth} {screenHeight}), MousePosition: ({x}, {y})')
			# 每个1s中打印一次 , 并执行清屏
			time.sleep(3)
			# 执行系统清屏指令
			os.system('cls')
	except KeyboardInterrupt:
		print('结束')

if __name__ == '__main__':
	main()
