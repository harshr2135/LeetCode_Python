# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        curr = head
        prev = None
        while curr!=tail:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        groupTail = head

        for i in range(k):
            if groupTail is None:
                return head
            groupTail = groupTail.next

        newHead = self.reverse(head, groupTail) 

        head.next = self.reverseKGroup(groupTail, k)

        return newHead        