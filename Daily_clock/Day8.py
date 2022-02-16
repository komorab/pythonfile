# 2022-2-16 1719 重构一棵树的方案
# 给你一个数组pairs ，其中pairs[i] = [xi, yi]，并且满足：
#   pairs中没有重复元素
#   xi < yi
# 令ways为满足下面条件的有根树的方案数：
#   树所包含的所有节点值都在 pairs中。
#   一个数对[xi, yi] 出现在pairs中当且仅当xi是yi的祖先或者yi是xi的祖先。
#   注意：构造出来的树不一定是二叉树。
# 两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。
# 请你返回：
#   如果ways == 0，返回0。
#   如果ways == 1，返回 1。
#   如果ways > 1，返回2。
# 一棵有根树指的是只有一个根节点的树，所有边都是从根往外的方向。
# 我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先。根节点没有祖先。

# 看不懂也不会写 复制了一个题解，放着吧
import collections

class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)
        ans = 1
        ancestors = set()
        for node in sorted(graph, key=lambda x: -len(graph[x])):
            parent = min(ancestors & graph[node], key=lambda x: len(graph[x]), default=None)
            ancestors.add(node)
            if parent:
                if graph[node] - (graph[parent] | {parent}):
                    return 0
                if len(graph[node]) == len(graph[parent]):
                    ans = 2
            elif len(graph[node]) != len(graph) - 1:
                return 0
        return ans


if __name__ == '__main__':
    pairs = [[1, 2], [2, 3]]
    a = Solution()
    print(a.checkWays(pairs))
