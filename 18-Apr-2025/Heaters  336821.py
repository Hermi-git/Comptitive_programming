# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l = 0
        r = max(abs(houses[0]-heaters[-1]), abs(houses[-1]-heaters[0]))
        ans = 0

        def warm(radius):
            ranges = []
            for heater in heaters:
                ranges.append([heater-radius, heater+radius])
            count =0
            i = j =0 
            while i < len(houses) and j < len(ranges):
                if houses[i] in range(ranges[j][0], ranges[j][-1]+1):
                    count += 1
                    i += 1
                else:
                    j += 1
            return count >= len(houses)
        while l <= r:
            mid = (l+r)//2
            if warm(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans 