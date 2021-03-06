# 2022-3-5 521 最长特殊序列
"""
给你两个字符串a和b，请返回 这两个字符串中 最长的特殊序列 的长度。如果不存在，则返回 -1。
「最长特殊序列」定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
字符串s的子序列是在从s中删除任意数量的字符后可以获得的字符串。
脑筋急转弯题目。。。
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
