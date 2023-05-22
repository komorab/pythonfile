# 23-5-8 for stack and so on test


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    """测试链表节点的命名域"""
    pre = head = ListNode(1)
    for i in range(2, 7):
        head.next = ListNode(i)
        head = head.next
    head.val = 29
    print(head.val)
    print(pre.next.next.next.next.next.val)
