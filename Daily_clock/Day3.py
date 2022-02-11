# 2022-2-11 学生分数的最小差值
# 给定数组 nums，nums[i] 表示第 i 个学生的分数，给定整数 k
# 从数组中选出任意 k 名学生的分数，使这 k 个分数间最高分和最低分的差值达到最小化 。返回可能的最小差值 。


class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        # 排序然后滑动求解
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
