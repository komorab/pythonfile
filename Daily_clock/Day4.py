"""
2022-2-12 leetcode 1020 飞地的数量：给定mxn数组，0代表海洋，1代表陆地，
在只能经过陆地的情况下，return不能通过陆地离开矩阵的点的数目
广度优先搜索(bfs)、深度优先搜索(dfs)、并查集
"""
# 标准解答，但是不通过，思路先放这


class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or vis[r][c]:
                return
            vis[r][c] = True
            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                dfs(x, y)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        return sum(grid[i][j] and not vis[i][j] for i in range(1, m - 1) for j in range(1, n - 1))
