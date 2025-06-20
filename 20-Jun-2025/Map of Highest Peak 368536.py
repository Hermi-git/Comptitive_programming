# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def inbound(row, col):
            return 0<=row<rows and 0<=col<cols
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    visited.add((r, c))
                    queue.append((r, c))
                    isWater[r][c] = 0
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_row = r+dr
                new_col = c+dc
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    isWater[new_row][new_col] = isWater[r][c] + 1
                    queue.append((new_row, new_col))
        return isWater