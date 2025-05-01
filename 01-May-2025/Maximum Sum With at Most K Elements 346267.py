# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        min_heap = []
        n = len(grid)
        for r in range(n):
            for c in range(limits[r]):
                val = max(grid[r])
                grid[r].remove(val)
                heapq.heappush(min_heap,-val)
        summ =0
        for i in range(k):
            summ += -(heapq.heappop(min_heap))
        return summ