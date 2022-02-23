# 2022-2-23 917 仅仅反转字母
# 其实字符串的操作也不太熟悉
"""
给你一个字符串 s ，根据下述规则反转字符串：
    所有非英文字母保留在原有位置。
    所有英文字母（小写或大写）位置反转。
返回反转后的 s 。
"""


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        alpha = [i for i in s if i.isalpha()]
        return ''.join([i if not i.isalpha() else alpha.pop() for i in s])
