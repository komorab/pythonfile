# 23-2-11

import math

n = [10, 50, 100, 500, 1000]
result = []
for i in n:
    sin_i = 1
    half_i = 1
    while i:
        sin_i = math.sin(sin_i)
        half_i /= 2
        i -= 1
    result.append([sin_i, half_i])
for i in result:
    print(i)
