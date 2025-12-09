# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        currNext = head.next

        head = currNext 

        while(curr and currNext):
            curr.next = currNext.next
            currNext.next = curr
            if prev:
                prev.next = currNext

            prev = curr
            curr = curr.next
            if curr:
                currNext = curr.next

        return head


