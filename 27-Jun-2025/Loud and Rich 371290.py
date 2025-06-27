# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * len(quiet)
        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()
        answer = list(range(len(quiet)))
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                loud_rich_person = answer[node]
                current_loud_neigh = answer[neigh]
                if quiet[loud_rich_person] < quiet[current_loud_neigh]:
                    answer[neigh] = loud_rich_person
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return answer