# 2022-3-7 504 七进制
"""
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
        negative = num < 0
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append('-')
        return ''.join(digits[::-1])
