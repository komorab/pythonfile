
import math

def pivotInteger(n: int) -> int:
    x = math.sqrt((n * n + n) / 2)
    if (x % 1) == 0:
        return n
    else:
        return -1

if __name__ == '__main__':
    j = []
    for i in range(1000000000):
        if pivotInteger(i) != -1:
            j.append(i)
    print(j)
