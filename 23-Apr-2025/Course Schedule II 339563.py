# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        answer = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
       
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            answer.append(course)

            for neigh in graph[course]:
                incoming[neigh] -= 1

                if incoming[neigh] == 0:
                    queue.append(neigh)
        if len(answer) != numCourses:
            return []
        return answer

