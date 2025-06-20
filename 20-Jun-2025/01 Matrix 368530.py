# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        queue = deque()

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    visited .add((r, c))
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_row = r+dr
                new_col = c+dc
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    mat[new_row][new_col] = mat[r][c] +1
                    queue.append((new_row, new_col))
        return mat

        
