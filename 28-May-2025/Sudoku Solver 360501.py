# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Optimized by precomputing row, column, and box constraints with sets to reduce repeated scanning.
        """
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        empties = []

        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    bi = (r // 3) * 3 + (c // 3)
                    boxes[bi].add(num)
                else:
                    empties.append((r, c))

        def backtrack(idx=0) -> bool:
            if idx == len(empties):
                return True

            r, c = empties[idx]
            bi = (r // 3) * 3 + (c // 3)
            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[bi]:
              
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[bi].add(num)

                    if backtrack(idx + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[bi].remove(num)

            return False

        backtrack()
