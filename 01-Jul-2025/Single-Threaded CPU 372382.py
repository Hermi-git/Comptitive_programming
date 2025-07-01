# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks_with_index = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        tasks_with_index.sort(key=lambda x: x[0])

        result = []
        min_heap = []  
        time = 0
        i = 0

        while len(result) < n:
           
            while i < n and tasks_with_index[i][0] <= time:
                enqueue, process, idx = tasks_with_index[i]
                heapq.heappush(min_heap, (process, idx))
                i += 1

            if min_heap:
                process, idx = heapq.heappop(min_heap)
                time += process
                result.append(idx)
            else:
              
                time = tasks_with_index[i][0]

        return result
