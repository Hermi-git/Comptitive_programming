# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1,0), (-1,0), (0,-1)]
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
         
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == '0':
                return
            grid[row][col] = "0"

            for dr, dc in directions:
                new_row = row+dr
                new_col = col+dc
                dfs(new_row, new_col)

        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands +=1
                    dfs(r, c)
        return islands

