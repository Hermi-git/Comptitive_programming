# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l =1
        r = max(piles)
        ans = 1
        def good(rate):
            total_time = 0
            for pile in piles:
                total_time += ceil(pile/rate)
            return total_time <= h
        while l<=r:
            mid = (l+r)//2
            if good(mid):
                ans = mid
                r = mid -1
            else:
                l = mid+1
        return ans 