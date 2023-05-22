# 23-3-10
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def reverseList(head: ListNode) -> ListNode:
    #     cur, pre = head, None
    #     while cur:
    #         tmp = cur.next # 暂存后继节点 cur.next
    #         cur.next = pre # 修改 next 引用指向
    #         pre = cur      # pre 暂存 cur
    #         cur = tmp      # cur 访问下一节点
    #     return pre

    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        ret = []
        result = fin =  head
        while head:
            ret.append(head.val)
            head = head.next
        ret = ret[::-1]
        for i in range(len(ret)):
            result.val = ret[i]
            result = result.next
        return fin


if __name__ == '__main__':
    pre = head = ListNode(1)
    for i in range(2, 7):
        head.next = ListNode(i)
        head = head.next
    fin = Solution.reverseList(pre)
    print(fin.next.val)