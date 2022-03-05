# 2022-3-6 2100 适合打劫银行的日子
# 这不是正确答案，不过好奇问题出在哪
"""
一群强盗准备打劫银行。给你一个下标从 0开始的整数数组security，security[i]是第 i天执勤警卫的数量。日子从 0开始编号。同时给你一个整数time。
如果第 i天满足以下所有条件，我们称它为一个适合打劫银行的日子：
第 i天前和后都分别至少有 time天。
第 i天前连续 time天警卫数目都是非递增的。
第 i天后连续 time天警卫数目都是非递减的。
更正式的，第 i 天是一个合适打劫银行的日子当且仅当：
security[i-time] >= security[i-time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time]
请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0开始）。返回的日子可以 任意顺序排列。
"""


class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        ans = []
        n = len(security)
        if n <= time * 2:
            return []
        if not time:
            return list(range(n))
        elif time == 1:
            for i in range(time, n - time):
                if security[i - 1] >= security[i] and security[i] <= security[i + 1]:
                    ans.append(i)
        else:
            for i in range(time, n - time):
                count = True
                if security[i - 1] >= security[i] and security[i] <= security[i + 1]:
                    count = True
                else:
                    count = False
                if count:
                    for j in range(time - 1):
                        if security[i - j - 1] < security[i - j]:
                            count = False
                            break
                if count:
                    for k in range(time - 1):
                        if security[k + 1 + i] > security[k + 2 + i]:
                            count = False
                            break
                if count:
                    ans.append(i)
        return ans
