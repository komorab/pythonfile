# 2022-2-15 1380 矩阵中的幸运数
# 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数
# 幸运数是指矩阵中满足同时下列两个条件的元素：
# 在同一行的所有元素中最小
# 在同一列的所有元素中最大

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        n = len(matrix[0])
        m = len(matrix)
        trans = [[matrix[a][b] for a in range(m)] for b in range(n)]
        # 转置，空间换时间 等于 trans = [i for i in zip(*matrix]
        for i in range(m):
            if max(trans[matrix[i].index(min(matrix[i]))]) == min(matrix[i]):
                ans.append(min(matrix[i]))
        return ans


"""
        rowMin = [min(i) for i in matrix]        
        colMax = [max(i) for i in zip(*matrix)]
        return [i for i in rowMin if i in colMax]
"""
