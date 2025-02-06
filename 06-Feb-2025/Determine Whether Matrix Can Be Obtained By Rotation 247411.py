# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if mat == target:  
                return True
            new_mat = [[0] * n for _ in range(n)]
            for row in range(n):
                for col in range(n):
                    new_mat[col][n - 1 - row] = mat[row][col] 
            mat = new_mat  

        return False  
