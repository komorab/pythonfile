# 2022-2-13
# 给定一个字符串 text，其中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        list_str = ['a', 'b', 'l', 'o', 'n']
        count = [0 for _ in range(5)]
        for s in range(len(list_str)):
            count[s] = text.count(list_str[s])
            if s == 2 or s == 3:
                count[s] = count[s] // 2
        return min(count)
