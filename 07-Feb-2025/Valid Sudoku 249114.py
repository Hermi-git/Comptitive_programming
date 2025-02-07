# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in rows[row] or board[row][col] in cols[col]or board[row][col] in sub_boxes[(row//3, col//3)]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sub_boxes[(row//3, col//3)].add(board[row][col])
        return True