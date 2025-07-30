# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        removed = 0
        min_set = 0
        half = len(arr)//2

        while removed < half:
            removed += -heapq.heappop(max_heap)
            min_set += 1
        return min_set
