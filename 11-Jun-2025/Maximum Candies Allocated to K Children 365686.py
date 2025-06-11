# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = sum(candies)

        def allocated(x):
            child =0 
            for candy in candies:
                child += (candy//x)
            return child >= k
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if allocated(mid):
                ans =mid
                low = mid +1
            else:
                high = mid -1
        return ans 