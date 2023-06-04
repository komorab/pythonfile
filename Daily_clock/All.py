# 23-5-27 做题合集
from typing import List


class Solution:
    # 1093. 大样本统计
    def sampleStats(self, count: List[int]) -> List[float]:
        mini = mid = maxi = -1 # 最大最小值
        most = [0, 0]
        sigma = 0
        cou = 0

        if sum(count) % 2 == 1:
            sign = 1
            mid_position = sum(count) // 2 + 1
        else:
            sign = 0
            mid_position = sum(count) / 2
            record = [-1, -1]


        for i in range(256):
            ii = float(i)
            if mini == -1 and count[i]:
                mini = ii

            if count[i]:
                maxi = ii

                if count[i] > most[0]:
                    most[0], most[1] = count[i], ii

                cou += count[i]
                if sign:
                    if cou >= mid_position and mid == -1:
                        mid = ii
                else:
                    if cou == mid_position:
                        record[1] = ii
                    if cou > mid_position and record[0] == -1:
                        record[0] = ii

            sigma += count[i] * i

        if not sign:
            if record[1] == -1:
                mid = record[0]
            else: mid = sum(record) / 2

        average = sigma / sum(count)

        print(sigma, cou)

        return [mini, maxi, average, mid, most[1]]

    # 1439. 有序矩阵中的第 k 个最小数组和
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        res = [0]
        for row in mat:
            res = sorted([x + r for x in row for r in res])[:k]
        return res[-1]
        #a = mat[0][:k]
        #for row in mat[1:]:
        #    a = sorted(x + y for x in a for y in row)[:k]
        #return a[-1]
        # 用时比上面多大概60ms，排除leetcode的随机因素，应该是因为切片，考虑切片的底层实现

    # 2455. 可被三整除的偶数的平均值
    def averageValue(self, nums: List[int]) -> int:
        return sum(i for i in nums if i % 6 == 0) // sum(j % 6 == 0 for j in nums) if sum(j % 6 == 0 for j in nums) else 0





if __name__ == '__main__':
    solution = Solution()
    test = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3510,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6718,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            27870,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26256,0,0,0,0,9586565,0,0,0,0,0,0,0,2333,0,0,0,0]
    print(solution.sampleStats(test))
