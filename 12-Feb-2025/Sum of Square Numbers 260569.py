# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool: 
        left =0
        right = int(math.sqrt(c))
        while left <= right:
            summ = left** 2 + right**2
            print(summ)
            if summ == c:
                return True
            if summ < c:
                left += 1
            else:
                right -= 1
        return False
        

