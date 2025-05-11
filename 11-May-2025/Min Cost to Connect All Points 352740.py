# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[]for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
    
        total_cost = 0
        visited = set()
        min_heap = [(0,0)]

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            visited.add(point)
            total_cost += cost

            for neigh_cost, neigh in adj[point]:
                if neigh not in visited:
                    heapq.heappush(min_heap, (neigh_cost, neigh))
        
        return total_cost

