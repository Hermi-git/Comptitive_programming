# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #  validate rows
        for r in range(9):
            s = set()
            for c in range(9):
                if board[r][c] in s:
                    return False
                elif board[r][c] != ".":
                    s.add(board[r][c])
        #  validate cols
        for r in range(9):
            s = set()
            for c in range(9):
                if board[c][r] in s:
                    return False
                elif board[c][r] != ".":
                    s.add(board[c][r])
        # validate 3 X 3 box
        starts = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]
        for i, j in starts:
            s = set()
            for r in range(i , i+3):
                for c in range(j, j+3):
                    if board[r][c] in s:
                        return False
                    elif board[r][c] != ".":
                        s.add(board[r][c])
        return True
        
                     

        
