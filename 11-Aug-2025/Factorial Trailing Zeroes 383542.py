# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # calculate the factorial of n
        def factorial(n):
            if n < 2:
                return 1
            return n* factorial(n-1)
    
        # calculate the trailing zeros
        fact_n = factorial(n)
        res = 0
        while fact_n % 10 == 0:
            res += 1
            fact_n //= 10
                
    
        return res