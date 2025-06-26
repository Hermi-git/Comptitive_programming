# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[]for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = []

        for pre, course in prerequisites:
            adj[pre].append(course)
            incoming[course] += 1
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            order.append(course)

            for neigh in adj[course]:
                incoming[neigh] -= 1

                if incoming[neigh] == 0:
                    queue.append(neigh)
        if len(order) != numCourses:
            order = []
        
        def dfs(node, visited):
            for neigh in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh, visited)
            return visited
        reachable = []
        for course in range(numCourses):
            reachables = dfs(course, set())
            reachable.append(list(reachables))
        answer = [False] * len(queries)
        for i in range(len(queries)):
            c1 = queries[i][0]
            c2 = queries[i][1]
            if c2 in reachable[c1]:
                answer[i] = True
        return answer
