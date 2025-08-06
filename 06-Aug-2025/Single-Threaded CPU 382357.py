# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        order = []
        time = tasks[0][0]
        min_heap = []
        i = 0
        while i < len(tasks) or min_heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i +=1

            if not min_heap:
                time = tasks[i][0]
            else:
                pros_time, idx = heapq.heappop(min_heap)
                time += pros_time
                order.append(idx)
        return order

    
