# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in enumerate(manager):
            graph[v].append(u)
        
        def dfs(employee):
            number_of_minutes = 0
            for neigh in graph[employee]:
                number_of_minutes = max(number_of_minutes, dfs(neigh))
            return informTime[employee] + number_of_minutes

        return dfs(headID)
        

