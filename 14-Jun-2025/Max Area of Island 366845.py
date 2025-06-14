# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1,0), (-1,0), (0,-1)]
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        areas =[0]
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0  # Mark this land as visited
            area = 1

            for dr, dc in directions:
                new_row = row+dr
                new_col = col+dc
                area += dfs(new_row, new_col)
            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    island = dfs(r, c)
                    areas.append(island)
        return max(areas)