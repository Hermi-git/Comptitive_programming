# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        for row in matrix:
            row.reverse()
        return matrix