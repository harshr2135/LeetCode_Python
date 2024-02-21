# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        result = head.val
        while head.next:
            result = result * 2 + head.next.val
            head = head.next
        return result
        

        # num = head
        # dec = 0

        # len = head
        # length = 0
        # while len is not None:
        #     length += 1
        #     len = len.next
    
        # while length != 0:
        #     length -= 1
        #     dec += num.val*(2**length)
        #     num = num.next
        # return dec