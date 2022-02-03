#2020-7-21
#给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        dct = {}

        def left_right(left: int, right: int):
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            ret = []
            for i in range(left, right+1):
                left_lst = left_right(left, i-1)
                right_lst = left_right(i+1, right)
                for L in left_lst:
                    for R in right_lst:
                        app_Tree = TreeNode(i)
                        app_Tree.left = L
                        app_Tree.right = R
                        ret.append(app_Tree)
            dct[(left, right)] = ret
            return ret
        left_right(1, n)
        return left_right(1, n)

if __name__ == '__main__':
    Solution.generateTrees(n = 3)