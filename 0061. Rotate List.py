# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        temp = head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        k = k%length
        if k == 0:
            return head

        rotate = length - k - 1    

        forwList, curr = head, head
        while rotate>0:
            curr = curr.next
            rotate -= 1

        backList = curr.next
        temp_back = backList
        curr.next = None

        while temp_back.next is not None:
            temp_back = temp_back.next

        temp_back.next = forwList

        return backList


