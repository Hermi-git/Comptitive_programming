# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for u, v in redEdges:
            red[u].append(v)
        
        for u, v in blueEdges:
            blue[u].append(v)
        
        answer = [-1] * n
        answer[0]= 0
        queue = deque([[0,0,None]])
        visited = set()
        visited.add((0, None))

        while queue:
            node, distance, edge_color = queue.popleft()

            if answer[node] == -1:
                answer[node] = distance
            
            if edge_color != "RED":
                for neigh in red[node]:
                    if (neigh, "RED") not in visited:
                        visited.add((neigh, "RED"))
                        queue.append([neigh, distance+1, "RED"])
            
            if edge_color != "BLUE":
                for neigh in blue[node]:
                    if (neigh, "BLUE") not in visited:
                        visited.add((neigh, "BLUE"))
                        queue.append([neigh, distance+1, "BLUE"])
        
        return answer
            

            