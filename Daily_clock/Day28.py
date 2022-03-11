# 2022-3-11 两题
"""
2049. 统计最高分的节点数目
给你一棵根节点为 0 的二叉树，它总共有 n个节点，节点编号为0到n - 1。同时给你一个下标从0开始的整数数组parents表示这棵树，
其中parents[i]是节点 i的父节点。由于节点 0是根，所以parents[0] == -1。
一个子树的 大小为这个子树内节点的数目。每个节点都有一个与之关联的分数。求出某个节点分数的方法是，
将这个节点和与它相连的边全部 删除，剩余部分是若干个 非空子树，这个节点的 分数为所有这些子树 大小的乘积。
请你返回有 最高得分节点的 数目。
"""
"""
589. N 叉树的前序遍历
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    @staticmethod
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)

        maxScore, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size
        dfs(0)
        return cnt

    @staticmethod
    def preorder(self, root: 'Node') -> list[int]:
        ans = []

        def dfs(node: 'Node'):
            if node is None:
                return
            ans.append(node.val)
            for ch in node.children:
                dfs(ch)
        dfs(root)
        return ans
