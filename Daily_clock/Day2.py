# 2022-2-9 两数之差
# 给定一个整数数组 nums 和一个整数 k ，返回数对 (i, j) 的数目，满足 i < j 且 |nums[i]-nums[j]| == k

class Solution(object):
    def countKDifference(self, nums, k) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(0, len(nums)):
            for a in range(i + 1, len(nums)):
                if abs(nums[i] - nums[a]) == k:
                    count += 1
        return count


if __name__ == '__main__':
    nums = [1, 2, 2, 1]
    k = 1
    ke = Solution()
    print(ke.countKDifference(nums, k))
