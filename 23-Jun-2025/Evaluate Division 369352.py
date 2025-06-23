# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, eq in enumerate(equations):
            u, v = eq
            w = values[idx]
            graph[u].append((v, w))
            graph[v].append((u, 1/w))

        answer = [-1.0] * len(queries)
        for i, query in enumerate(queries):
            dividend, divisor = query
            if dividend not in graph or divisor not in graph:
                continue
            q = deque([(dividend, 1)])
            visited = set()
            visited.add(dividend)
            while q:
                node, w = q.popleft()
                if node == divisor:
                    answer[i] = w
                for neigh, weigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append((neigh, w * weigh))
        
        return answer
