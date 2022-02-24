# 2022-2-24 1706 球会落何处
# 整体思路还是很简单，除了会出现一些奇怪的bug
"""
用一个大小为 m x n 的二维网格 grid 表示一个箱子。你有 n 颗球。箱子的顶部和底部都是开着的。
箱子中的每个单元格都有一个对角线挡板，跨过单元格的两个角，可以将球导向左侧或者右侧。
    将球导向右侧的挡板跨过左上角和右下角，在网格中用 1 表示。
    将球导向左侧的挡板跨过右上角和左下角，在网格中用 -1 表示。
在箱子每一列的顶端各放一颗球。每颗球都可能卡在箱子里或从底部掉出来。如果球恰好卡在两块挡板之间的 "V" 形图案，
或者被一块挡导向到箱子的任意一侧边上，就会卡住。
返回一个大小为 n 的数组 answer ，其中 answer[i] 是球放在顶部的第 i 列后从底部掉出来的那一列对应的下标，
如果球卡在盒子里，则返回 -1 。
"""


class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        n = len(grid[0])
        m = len(grid)
        if n == 1:
            return [-1]
        for i in range(n):
            count = i
            for j in range(m):
                if grid[j][count] == 1:
                    if count == n-1 or grid[j][count+1] == -1:
                        answer.append(-1)
                        break
                    count += 1
                elif grid[j][count] == -1:
                    if count == 0 or grid[j][count-1] == 1:
                        answer.append(-1)
                        break
                    count -= 1
                if j == m-1:
                    answer.append(count)
        return answer
