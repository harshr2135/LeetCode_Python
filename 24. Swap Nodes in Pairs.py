# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        cur = head
        new = head.next

        while cur and cur.next:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = cur
            cur = cur.next
            if cur and cur.next:
                temp.next.next = cur.next

        return new