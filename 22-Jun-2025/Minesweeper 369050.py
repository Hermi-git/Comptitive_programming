# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        def inbound(row, col):
            return 0<=row<m and 0<=col<n
        
        def count_adj_mine(row, col):
            count = 0
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if inbound(new_r, new_c) and board[new_r][new_c] =="M":
                    count+=1
            return count
        r, c = click
        visited = set()
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            r, c = q.popleft()
            if board[r][c] == "M":
                board[r][c] = "X"
                return board
            count_mine = count_adj_mine(r, c)
            if count_mine > 0 :
                board[r][c] = str(count_mine)
            else:
                board[r][c] = "B"
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc
                    count_mine = 0
                    if inbound(new_r, new_c) and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
                
        return board




