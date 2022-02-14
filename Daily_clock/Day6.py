# 2022-2-14 给定数组nums，有序排列2n + 1个正整数
# 其中每个元素都会出现两次，唯有一个数只会出现一次。找出该数

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = (len(nums) // 2) * 2
        for i in range(0, count, 2):
            if nums[i] == nums[i+1]:
                continue
            else:
                return nums[i]
        return nums[-1]
