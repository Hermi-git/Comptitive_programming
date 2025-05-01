# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v , time in times:
            graph[u].append((v, time))
        
        min_times = {}
        min_heap = [(0, k)]  

        while min_heap:
            time_k_to_node, node = heapq.heappop(min_heap)
            if node in min_times:
                continue
            min_times[node] = time_k_to_node
            for neigh, neigh_time in graph[node]:
                if neigh not in min_times:
                    heapq.heappush(min_heap, (time_k_to_node + neigh_time, neigh))
        return max(min_times.values()) if len(min_times) == n else -1
        
       