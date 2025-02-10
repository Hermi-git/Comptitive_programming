# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m-1):
            for col in range(n-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True 
