# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = ceil(x/2)

        while low <= high:
            mid = (low+high)//2
            if mid * mid <= x:
                low = mid + 1
            else:
                high = mid -1
        return high


