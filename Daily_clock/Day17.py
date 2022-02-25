# 2022-2-25 537 复数乘法
# 虽然中难度但是？
"""
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
    实部 是一个整数，取值范围是 [-100, 100]
    虚部 也是一个整数，取值范围是 [-100, 100]
    i^2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。
"""


class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1.split('+')
        num2 = num2.split('+')
        real = int(num1[0]) * int(num2[0]) - int(num1[1][:-1]) * int(num2[1][:-1])
        image = int(num1[0]) * int(num2[1][:-1]) + int(num1[1][:-1]) * int(num2[0])
        return str(real) + '+' + str(image) + 'i'
