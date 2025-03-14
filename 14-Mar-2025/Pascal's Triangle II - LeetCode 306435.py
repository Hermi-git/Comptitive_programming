# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate_row(n):
            if n== 0:
                return []
            if n == 1:
                return [1]
            if n == 2:
                return [1, 1]
            prev_row = generate_row(n-1)
            cur_row=[1]*(len(prev_row)+1)
            for i in range(1, n-1):
                cur_row[i]=prev_row[i-1]+prev_row[i]
            prev_row=cur_row
            return prev_row

            
        return generate_row(rowIndex+1)
      
            


            
        
        