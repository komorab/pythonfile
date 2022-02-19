# 2022-2-19 969 煎饼排序
# 给定数组arr以及整数k，将arr的前k项翻转 0 - k-1转k-1 - 0并返回arr（k可以为None，或者不止一个
# 不太明白，不是应该有个k吗，没有k的输入怎么翻转前k项？


class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in range(len(arr), 1, -1):
            index = 0
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            if index == n - 1:
                continue
            m = index
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]  # 原地反转
            for i in range(n // 2):
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]  # 原地反转
            ans.append(index + 1)
            ans.append(n)
        return ans
