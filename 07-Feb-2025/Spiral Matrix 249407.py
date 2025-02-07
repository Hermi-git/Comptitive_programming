# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top, left = 0, 0
        right, down = n-1, m-1

        result = []
        while left <= right and top <= down:
            
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  

            
            for row in range(top, down + 1):
                result.append(matrix[row][right])
            right -= 1 

            if top <= down:  
                for col in range(right, left - 1, -1):
                    result.append(matrix[down][col])
                down -= 1  

            if left <= right:  
                for row in range(down, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  
        return result



