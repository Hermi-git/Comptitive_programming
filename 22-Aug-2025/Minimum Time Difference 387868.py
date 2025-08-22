# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time_str):
            hrs, min = map(int, time_str.split(":"))
            total_min = hrs * 60 + min
            return total_min 

        minute = sorted(time_to_minutes(timePoint) for timePoint in timePoints)
        
        n = len(timePoints)
        min_diff = float('inf')
        for i in range(n-1):  
            curr =  minute[i + 1] - minute[i]
            min_diff = min(min_diff, curr)
        circular_diff = (minute[0] + 1440) - minute[-1]
        min_diff = min(min_diff, circular_diff)

        return min_diff
        
