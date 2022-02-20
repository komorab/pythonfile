# 模拟随机试验

import random
import numpy
import matplotlib.pyplot as pyplot


def roll_dice():
    """模拟扔骰子结果"""
    roll = random.randrange(1, 7)
    return roll


def main():
    times = int(input('The times of roll:'))
    total_times = list(range(1, times+1))
    result = []  # 全部实验的结果
    each_times = [0, 0, 0, 0, 0, 0]  # 每个数字出现的频数
    for each in total_times:
        res = roll_dice()
        result.append(res)
        for i in range(1, 7):
            if res == i:
                each_times[i-1] += 1
    numlist = list(range(1, 7))
    print('一共{}次，'.format(times))
    for x in range(6):
        print(numlist[x], end=' ')
        print(each_times[x])
    y = numpy.array(result)
    pyplot.hist(y, bins=6)
    pyplot.title('the plot of test')
    pyplot.xlabel('point')
    pyplot.ylabel('times')
    pyplot.show()


if __name__ == '__main__':
    main()
