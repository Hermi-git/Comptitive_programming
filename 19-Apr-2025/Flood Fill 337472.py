# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        copy_image = [row[:] for row in image]
        init_color = image[sr][sc]
        if init_color == color:
            return copy_image
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(image), len(image[0])  
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def dfs(x, y):
            copy_image[x][y] = color
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (is_inbound(new_x, new_y)
                    and image[new_x][new_y] == init_color
                    and copy_image[new_x][new_y] != color):
                    dfs(new_x, new_y)

        dfs(sr, sc)
        return copy_image