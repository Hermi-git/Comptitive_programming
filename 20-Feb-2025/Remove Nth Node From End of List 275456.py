# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        length = 0
        while current.next:
            current = current.next
            length += 1

        current = dummy
        size = length -n 
        i = 0
        while current and i < size:
            current = current.next
            i += 1
    
        current.next = current.next.next
        return dummy.next
        

        