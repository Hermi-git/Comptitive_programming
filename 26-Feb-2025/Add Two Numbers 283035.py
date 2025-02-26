# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        num1 = ""
        num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        summ = int(num1[::-1]) + int(num2[::-1])
        val = str(summ)
        for num in val[::-1]:
            res.append(int(num))

        dummy = ListNode(-1)
        curr = dummy

        for num in res:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next      