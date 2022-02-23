# 2022-2-22 1994 好子集的数目
# 2022-2-23 失败了，问题在哪？
"""
给你一个整数数组nums。如果nums的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为好子集。
比方说，如果nums = [1, 2, 3, 4]：
[2, 3]，[1, 2, 3]和[1, 3]是 好子集，乘积分别为6 = 2*3，6 = 2*3和3 = 3。
[1, 4] 和[4]不是 好子集，因为乘积分别为4 = 2*2 和4 = 2*2。
请你返回 nums中不同的好子集的数目对10^9 + 7取余的结果。
nums中的 子集是通过删除 nums中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，
那么它们被视为不同的子集。
"""
from collections import Counter, defaultdict


class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type: nums: List[int]
        :rtype: int
        """
        useful = Counter(nums)
        mod = 10 ** 9 + 7
        prime = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        tprime = [6, 10, 14, 15, 21, 22, 26]
        whole = list(range(1, 31))
        for i in whole:
            if i in prime or i in tprime:
                continue
            else:
                del useful[i]
        count = 0
        # 只用质数 要考虑到1不是质数

        def d(n):
            num = 1
            for i in range(1, n+1):
                num *= i
            return num

        def c(m, n):
            return d(n)/(d(m)*d(n-m))

        a = [c(i, 10) for i in range(1, 11)]
        count += sum(a)
        for i in prime:
            if not useful[i]:
                count *= useful[i]
        # 非质数部分
        for num in tprime:
            dprime = prime[1:]
            for dp in dprime:
                if num % dp == 0:
                    del dprime[dprime.index(dp)]
            dprime.append(num)
            dprime.append(1)
            b = [c(i, 8) for i in range(9)]
            count += sum(b)
            for i in prime:
                if not useful[i]:
                    count *= useful[i]

        return count % mod


if __name__ == '__main__':
    aka = Solution()
    print(aka.numberOfGoodSubsets([1, 2, 3, 4]))
