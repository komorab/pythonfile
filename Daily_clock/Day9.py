# 2022-2-17 688 骑士在棋盘上的概率
# 在一个n x n的国际象棋棋盘上，一个骑士从单元格 (row, column)开始
# 并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
# 象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
# 骑士继续移动，每一步都会在八种方向随机选择一种，直到它走了k步或离开了棋盘。
# 返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。
# 还是不会，涉及线代，大脑空白


class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                dp[step][i][j] += dp[step - 1][ni][nj] / 8
        return dp[k][row][column]
