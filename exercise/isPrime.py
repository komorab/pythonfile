# 2022-2-22 用于判断一个数是否是质数
import random


def is_prime(num: int) -> bool:
    """判断给定的数是否是质数"""
    if num in [1, 2, 3]:
        return True
    elif num > 1:
        mod = num % 6
        if mod == 1 or mod == 5:
            for i in range(5, int(num ** 0.5) + 1, 6):
                if num % i == 0:
                    return False
            return True
        return False


def list_prime(num_list: list):
    """
    判断给定的数组中的每一项是否为质数
    并返回由布尔值组成的数组
    :rtype: list[bool]
    """
    value = []
    for i in num_list:
        if is_prime(i):
            value.append(True)
        else:
            value.append(False)
    return value


if __name__ == '__main__':
    num = [random.randint(2, 100000) for _ in range(20)]
    num = [i for i in num if is_prime(i)]
    print(num)
