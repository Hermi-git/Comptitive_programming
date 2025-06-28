# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [i for i in range(n)]
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        leaves = [node for node in range(n) if degree[node] == 1]
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves =[]

            for leaf in leaves:
                for neigh in graph[leaf]:
                    degree[neigh] -= 1
                    if degree[neigh] == 1:
                        new_leaves.append(neigh)
            leaves = new_leaves

        return leaves