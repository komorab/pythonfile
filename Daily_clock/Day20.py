# 2022-3-2 564 寻找最近的回文数
"""
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
“最近的”定义为两个整数差的绝对值最小。
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return f'{int(n) - 1}'
        if length % 2 == 1:
            header = n[:length // 2]
            palindrome = [int(f'{header}{j}{header[::-1]}') for j in range(10)]
        else:
            header = n[:length // 2 - 1]
            palindrome = [int(f'{header}{i}{i}{header[::-1]}') for i in range(10)]
        if int(n) in palindrome:
            del palindrome[palindrome.index(int(n))]
        result = list(map(lambda x, y: abs(x - y), palindrome, [int(n) for _ in range(10)]))
        if abs(int(n) - int('9' * (length - 1))) <= min(result):
            return '9' * (length - 1)
        elif abs(int(n) - pow(10, length) + 1) < min(result):
            return str(pow(10, length) + 1)
        return str(palindrome[result.index(min(result))])
