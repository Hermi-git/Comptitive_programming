# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[v].append(u) 
        WHITE = 0
        GRAY = 1
        BLACK = 2
        color = [WHITE] * numCourses 
        def dfs(node):
            color[node] = GRAY
            result = True
            for neighbor in adj_list[node]:
                if color[neighbor] == GRAY:
                    return False 
                elif color[neighbor] == WHITE:
                    result = result and dfs(neighbor)      
            color[node] = BLACK
            return result
        ans  = True
        for course in range(numCourses):
            if color[course] == WHITE:
                ans = ans and dfs(course)  
        return ans  
