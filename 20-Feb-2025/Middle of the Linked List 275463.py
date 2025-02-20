# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy 
        length = 0

        while current.next:
            current = current.next
            length += 1
        
        current = dummy
        for _ in range(length//2):
            current = current.next
        return current.next
