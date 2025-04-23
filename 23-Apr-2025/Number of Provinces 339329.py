# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visited = set()
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    adj_list[r].append(c)
               
        def dfs(city):
            for neigh in adj_list[city]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
            
        province = 0
        for node in range(len(isConnected)):
            if node not in visited:
                visited.add(node)
                dfs(node)
                province += 1
        return province 
                


