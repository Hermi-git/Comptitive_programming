# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = sum(candies)

        def validate(x):
            child =0 
            for candy in candies:
                child += (candy//x)
            return child >= k
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if validate(mid):
                ans =mid
                l = mid +1
            else:
                r = mid -1
        return ans 