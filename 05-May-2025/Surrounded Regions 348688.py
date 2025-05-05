# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()
        directions = [(0, 1), (1,0), (-1,0), (0,-1)]
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        def dfs(row, col):
            visited.add((row, col))
            board[row][col] = "T"

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if inbound(new_row, new_col) and board[new_row][new_col] == "O" and (new_row, new_col) not in visited :
                    dfs(new_row, new_col)
        
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n-1] == "O":
                dfs(r, n-1)
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m-1][c] == "O":
                dfs(m-1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"




       