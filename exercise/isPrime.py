# 2022-2-22 用于判断一个数是否是质数
# 23-3-2 2021判断错误 需要修正

def is_prime(num: int) -> bool:
    """判断给定的数是否是质数"""
    if num in [1, 2, 3]:
        return True
    elif num > 3:
        mod = num % 6
        if mod == 1 or mod == 5:
            for i in range(5, int(num ** 0.5) + 1, 6):
                if num % i == 0:
                    return False
            return True
        return False

def isPrime(num: int) -> bool:
    """粗暴判断质数"""
    if num in [1, 2, 3]:
        return True
    elif num > 3:
        for _ in range(2, int(num ** 0.5) + 1):
            if not (num % _):
                return False
        return True


if __name__ == '__main__':
    print(isPrime(19))