# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = 1, 2
        fresh_oranges = 0
        minutes = -1
        q = deque()
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == fresh:
                    fresh_oranges += 1
                elif grid[r][c] == rotten:
                    q.append((r,c))
        if fresh_oranges == 0:
            return 0
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if inbound(row, col) and grid[row][col] == fresh:
                        grid[row][col] = rotten
                        fresh_oranges -= 1
                        q.append((row, col))
            minutes += 1

        return minutes if fresh_oranges ==0 else -1
            
