# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        heap = nums[:]
        min_ops =0
        while len(heap) >= 2 and heap[0] < k:
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            heapq.heappush(heap, (val1 * 2 ) + val2)
            min_ops += 1
        return min_ops