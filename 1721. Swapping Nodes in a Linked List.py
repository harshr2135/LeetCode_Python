# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        firstPtr = head
        for i in range(1, k):
            firstPtr = firstPtr.next

        k_beg = firstPtr

        secondPtr = head
        while firstPtr.next is not None:
            secondPtr = secondPtr.next
            firstPtr = firstPtr.next

        k_end = secondPtr

        k_beg.val, k_end.val = k_end.val, k_beg.val

        return head