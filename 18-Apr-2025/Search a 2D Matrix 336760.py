# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for row in range(n):
            l =0
            r = m-1

            while l <= r:
                mid = (l+r)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid+1
                else:
                    r = mid-1

        return False