# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        dummy = ListNode()
        cur = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        return dummy.next
