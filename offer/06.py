# 23-3-10

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        # return self.reversePrint(head.next) + [head.val] if head else [] # 递归写法
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
