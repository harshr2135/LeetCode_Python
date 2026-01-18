# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList (self, head, tail):
        prev = None
        curr = head
        while prev != tail:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prevNode = None
        curr = head
        currIdx = 1

        while currIdx < left:
            prevNode = curr
            curr = curr.next
            currIdx += 1

        leftPrev = prevNode
        subHead = curr

        
        while currIdx < right:
            curr = curr.next
            currIdx += 1

        subTail = curr
        subListNext = subTail.next

        revSublist = self.reverseList(subHead, subTail)

        if leftPrev:
            leftPrev.next = revSublist
        else:
            head = revSublist

        subHead.next = subListNext

        return head  