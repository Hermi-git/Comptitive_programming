# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m+n -1)]

        # insert the elments of diagonals with their respective list
        for r in range(m):
            for c in range(n):
                diagonals[r+c].append(mat[r][c])
        result = diagonals[0]
        for i in range(1, len(diagonals)):
            if i % 2 == 1:
                result.extend(diagonals[i])
            else:
                result.extend(diagonals[i][::-1])
        return result