# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        perimeter = 0
        def dfs(row, col):
            nonlocal perimeter
            visited.add((row, col))

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1
                elif (new_row, new_col) not in visited:
                    dfs(new_row, new_col)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dfs(r, c)
                    return perimeter
        return 0
                