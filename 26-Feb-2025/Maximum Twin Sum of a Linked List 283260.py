# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        summ = 0
        max_sum = 0
        for i in range(len(arr)//2):
            val = arr[len(arr) - 1 - i]
            summ = val + arr[i]
            max_sum = max(max_sum, summ)
        return max_sum
        

