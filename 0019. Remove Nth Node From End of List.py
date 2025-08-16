# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head

        count = 0
        while temp is not None:
            count+=1
            temp = temp.next

        pos = count-n

        if pos == 0:
            return head.next
            
        prev = None
        curr = head
        while pos>0:
            prev = curr
            curr = curr.next
            pos-=1

        prev.next = curr.next

        return head