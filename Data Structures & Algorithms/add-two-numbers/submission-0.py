# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0)
        remainder = 0
        current = result

        while l1 or l2 or remainder :

            left1 = 0
            left2 = 0

            if l1:
                left1 = l1.val
                l1 = l1.next

            if l2:
                left2 = l2.val
                l2 = l2.next
            
            total = left1 + left2 + remainder

            remainder = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

        return result.next


        