# 2023-1-7 1658 将 x 减到 0 的最小操作数
"""
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。
请注意，需要 修改 数组以供接下来的操作使用。
如果可以将 x恰好 减到0 ，返回 最小操作数 ；否则，返回 -1 。
"""


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)

        if total < x:
            return -1

        right = 0
        lsum, rsum = 0, total
        ans = n + 1
        for left in range(-1, n - 1):
            if left != -1:
                lsum += nums[left]
            while right < n and lsum + rsum > x:
                rsum -= nums[right]
                right += 1
            if lsum + rsum == x:
                ans = min(ans, (left + 1) + (n - right))

        return -1 if ans > n else ans


if "name" == "main":
    nums = [1, 1, 4, 2, 3]
    x = 5
    a=Solution
    print(a.minOperations(nums, x))
