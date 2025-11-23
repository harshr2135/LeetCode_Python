# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = {}
        idx = 0
        curr = head
        while curr:
            if curr in hashset:
                return curr

            hashset[curr] = idx
            curr = curr.next
            idx+=1

        return None