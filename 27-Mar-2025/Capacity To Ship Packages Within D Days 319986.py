# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = None

        def validate(target):
            count_day = 1
            summ = 0
            for weight in weights:
                if summ + weight > target:
                    count_day += 1
                    summ = 0
                elif summ + weight == target:
                    summ = summ
                summ += weight
            return count_day <= days

        while low <= high:
            mid = (low+high)//2
            if validate(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans


