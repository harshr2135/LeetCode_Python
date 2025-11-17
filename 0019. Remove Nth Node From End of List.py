# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        beg = head

        while n>0:
            beg = beg.next
            n -= 1

        end = head
        prev = None

        if beg is None:
            return head.next

        while beg:
            prev = end
            end = end.next
            beg = beg.next

        prev.next = end.next
        end.next = None

        return head