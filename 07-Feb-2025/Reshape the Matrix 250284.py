# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if r * c != m * n:
            return mat
        
        one_D = [0] * (m*n)
        for row in range(m):
            for col in range(n):
                idx = row * n + col 
                one_D[idx] = mat[row][col]
        
        two_D = [[0] * c for _ in range(r)]
        for i in range(len(one_D)):
            two_D[i//c][i%c] = one_D[i]

        return two_D
        