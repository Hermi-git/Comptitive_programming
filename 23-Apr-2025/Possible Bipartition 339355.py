# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)
        color = [-1 for _ in range(n+1)]
        visited = set()
        def dfs(node):
            for neigh in adj_list[node]:
                if neigh in visited:
                    if color[neigh] == color[node]:
                        return False
                else:
                    if color[neigh] == -1:
                        if color[node] == 0:
                            color[neigh] = 1
                        else:
                            color[neigh] = 0
                        visited.add(neigh)
                        result = dfs(neigh)
                        if not result:
                            return False
            return True

        for node in range(n):
            if color[node] ==-1:
                visited.add(node)
                color[node] = 0
                if not dfs(node):
                    return False
        return True

   