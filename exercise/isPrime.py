# 2022-2-22 用于判断一个数是否是质数


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
