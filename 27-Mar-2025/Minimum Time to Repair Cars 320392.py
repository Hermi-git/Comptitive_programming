# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = max(ranks) * ((cars) ** 2)
        ans = None

        def minimum_time(time):
            total_time =0
            for rank in ranks:
                total_time += int(sqrt(time/rank))
            return total_time >= cars

        while low <= high:
            mid = (low+high)//2

            if minimum_time(mid):
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans