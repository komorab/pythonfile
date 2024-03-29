# 23-3-3
# fibonacci
# 23-5-11 and other things about math
from functools import lru_cache
import decimal


@lru_cache
def fibo(num: int) -> int:
    if num == 1 or num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


def factorial(n: int) -> int :
    """阶乘"""
    if n == 0:
        return 1
    elif n > 0:
        total = 1
        for i in range(1, n + 1):
            total *= i
        return total


def exp(n: int) -> float:
    """
    n表示泰勒展开的项数
    泰勒展开计算e的数值
    python的精度计算到18项会收敛
    值为2.7182818284590455
    """
    e = 1
    for _ in range(1, n + 1):
        e += 1 / factorial(_)
    return e


def expPrecision():
    precision = 20000
    decimal.getcontext().prec = precision
    e = decimal.Decimal(0)
    nFrac = decimal.Decimal(1)
    for n in range(1, precision + 1):
        e += nFrac
        nFrac /= n
    return e


if __name__ == '__main__':
    with open("e", "a") as f:
        f.write(f'{expPrecision()}\n')
