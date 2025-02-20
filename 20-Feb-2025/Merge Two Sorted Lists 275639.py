# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []

        while list1:
            merged.append(list1.val)
            list1 = list1.next
        
        while list2:
            merged.append(list2.val)
            list2 = list2.next

        merged.sort()
        
        dummy = ListNode(-1)
        current = dummy

        for num in merged:
            current.next = ListNode(num)
            current = current.next
        
        return dummy.next