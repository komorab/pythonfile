# 2022-3-8 2055 蜡烛之间的盘子数量
"""
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0开始的字符串s，它只包含字符'*' 和'|'，其中'*'表示一个 盘子，'|'表示一支蜡烛。
同时给你一个下标从 0开始的二维整数数组queries，其中queries[i] = [left i, right i]表示 子字符串s[left i...right i]（包含左右端点的字符）。
对于每个查询，你需要找到 子字符串中在 两支蜡烛之间的盘子的 数目。如果一个盘子在 子字符串中左边和右边 都至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间。
比方说，s = "||**||**|*"，查询[3, 8]，表示的是子字符串"*||**|"。子字符串中在两支蜡烛之间的盘子数目为2，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组answer，其中answer[i]是第i个查询的答案。
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        def count_plates(p: str) -> int:
            if p.count('|') < 2:
                return 0
            else:
                n, begin, end = len(p), 0, len(p) - 1
                for i in range(n):
                    if p[i] == '|':
                        begin = i
                        break
                for j in range(n-1, 0, -1):
                    if p[j] == '|':
                        end = j
                        break
                return p[begin:end].count('*')
        count = [] * len(queries)
        for i, j in enumerate(queries):
            count[i] = count_plates(s[j[0]:j[1]+1])
        return count

    def right_answer(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l

        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if 0 <= x < y and y >= 0:
                ans[i] = preSum[y] - preSum[x]
        return ans
