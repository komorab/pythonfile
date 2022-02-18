# 2022-2-18 1791 找出星形图的中心
# 对n个数构成的星形图，给定 n-1 项数组，每项代表一条边的两数，返回星形图的中心


class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]
