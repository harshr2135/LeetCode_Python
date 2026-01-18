# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        revSecondHalf = self.reverseList(slow)

        firstHalf = head

        while revSecondHalf:
            if firstHalf.val != revSecondHalf.val:
                return False
            
            firstHalf = firstHalf.next
            revSecondHalf = revSecondHalf.next

        return True