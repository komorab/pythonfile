# 2022-3-3 258 各位相加
"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
执行用时：36 ms, 在所有 Python3 提交中击败了63.13%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了48.79%的用户
"""


class Solution:
    @staticmethod
    def addDigits(self, num: int) -> int:
        def addnum(count: int) -> int:
            return sum([int(i) for i in str(count)])
        ret = addnum(num)
        while ret // 10:
            ret = addnum(ret)
        return ret

    @staticmethod
    def math_method(self, num: int) -> int:
        """数学方法"""
        return (num - 1) % 9 + 1 if num else 0
