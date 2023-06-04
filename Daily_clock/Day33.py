# 23-5-26 1091. 二进制矩阵中的最短路径
"""
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

路径途经的所有单元格的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。
"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        length = len(grid)
        if length == 1:
            return 1
        que = deque()
        visited = {}
        que.appendleft((0,0))
        visited[(0,0)] = True
        start = 1
        while que:
            for _ in range(len(que)):
                ind, con = que.pop()
                for pos_h, pos_v in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:
                    new_ind = ind + pos_h
                    new_con = con + pos_v
                    if length > new_ind >= 0 == grid[new_ind][new_con] and 0 <= new_con < length \
                            and not visited.get((new_ind, new_con)):
                        # 0 <= new_ind < length and 0 <= new_con < length and grid[new_ind][new_con] == 0
                        if new_ind == length - 1 and new_con == length - 1:
                            return start + 1
                        que.appendleft((new_ind, new_con))
                        visited[(new_ind, new_con)] = True
            start += 1
        return -1
