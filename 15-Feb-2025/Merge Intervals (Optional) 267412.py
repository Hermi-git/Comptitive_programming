# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result =[intervals[0]]

        for i in range(1, len(intervals)):
            start1, end1 = intervals[i]
            prev_start, prev_end = result[-1]

            if prev_end >= start1:
                result[-1][1] = max(prev_end, end1)
            else:
                result.append([start1, end1])
        return result