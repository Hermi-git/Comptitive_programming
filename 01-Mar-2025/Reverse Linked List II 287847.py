# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head 
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        nxt = None
        first_reverse = curr
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next= prev
            prev = curr
            curr = nxt
        first_reverse.next = curr
        prev_node = dummy
        while prev_node.next and prev_node.next != first_reverse:
            prev_node = prev_node.next
        prev_node.next = prev

        return dummy.next
        
        
     