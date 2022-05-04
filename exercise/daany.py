# 2022-5-2 处理excel数据
import math
from numpy import random
from math import *
from scipy.stats import *


day = 114


def c_wave(x, y) -> float:
    return (y - x)/x


def stdev_s(num:list) -> float:
    average = sum(num)/len(num)
    sq = []
    for i in num:
        sq.append(pow((i - average), 2))
    return math.sqrt(sum(sq)/(len(num) - 1))


def black_scholes(price, wave, time, riskfree=0.00009) -> float:
    return price * math.exp((riskfree - 0.5 * pow(wave, 2)) * time + wave * math.sqrt(time) * random.randn())


def day_record(price, wave, time, ct=4900) -> float:
    record = []
    for _ in range(1000):
        st = black_scholes(price, wave, time)
        if st <= ct:
            record.append(0)
        else:
            record.append(st - ct)
    return sum(record)/1000


def bs_call_value(target_price, strike_price, rf_rate, maturity, volatility):
    d1 = log(target_price/strike_price, e) + (rf_rate + pow(volatility, 2))*maturity
    d1 = d1/(volatility * maturity ** 0.5)
    d2 = d1 - volatility * maturity ** 0.5
    '''call_value = target_price * norm.cdf(d1, 0, 1) - strike_price * pow(e, -rf_rate * maturity) * norm.cdf(d2, 0, 1)'''
    return target_price * norm.cdf(d1, 0, 1) - strike_price * pow(e, -rf_rate * maturity) * norm.cdf(d2, 0, 1)


with open(r'G:\PycharmProject\pythonfile\exercise\data.txt', 'r') as f:
    data = f.read()
data = data.replace('\n', ',')
n_data = data.split(',')
close = n_data[1::2]
for j in range(len(close)):
    close[j] = float(close[j])

wave = []
for i in range(len(close) - 1):
    wave.append(c_wave(close[i], close[i+1]))

stdev = []
for k in range(250, len(wave)):
    stdev.append(stdev_s(wave[k-250:k]))

ans = [i*math.sqrt(250) for i in stdev]

call = []
count = 0
for n in range(113, -1, -1):
    call.append(day_record(close[count + 251], ans[count], n/250))
    count += 1


with open(r'G:\PycharmProject\pythonfile\exercise\end_price', 'r') as f:
    call_value = f.read()
call_value = call_value.replace('\n', ',')
call_value = call_value.split(',')
call_value.pop()
for _ in range(len(call_value)):
    call_value[_] = float(call_value[_])
strike_price = 4900
rf_rate = 0.00009
maturity = [n/250 for n in range(113, -1, -1)]
target_price = close[251:]
implied = []

for n in range(113):
    i, j, k = call_value[n], maturity[n], target_price[n]
    rang = [0.1, 0.9]
    while 1:
        mid = sum(rang) / 2
        end = [bs_call_value(k, strike_price, rf_rate, j, rang[0]), bs_call_value(k, strike_price, rf_rate, j, rang[1]),
               bs_call_value(k, strike_price, rf_rate, j, mid)]

        if abs(end[0] - i) <= 0.00001:
            implied.append(rang[0])
            break
        elif abs(end[1] - i) <= 0.00001:
            implied.append(rang[1])
            break
        elif abs(end[-1] - i) <= 0.00001:
            implied.append(mid)
            break

        if (end[0] - i) * (end[-1] - i) < 0:
            rang[1] = mid
        else:
            rang[0] = mid


if __name__ == '__main__':
    for _ in implied:
        print(_)