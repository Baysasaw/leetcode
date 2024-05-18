# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = head
        second = head
        for i in range(k-1):
            first = first.next
        temp = first
        first = first.next
        while first:
            first = first.next
            second = second.next
        temp.val, second.val = second.val, temp.val
        return head