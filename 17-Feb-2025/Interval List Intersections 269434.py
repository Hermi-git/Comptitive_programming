# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        l, r = 0, 0
        result = []
        while l < len(firstList) and r< len(secondList):
            start1, end1 = firstList[l]
            start2, end2 = secondList[r]

            if start1 > end2:
                r += 1
            elif start2 > end1:
                l += 1
            
            else:
                result.append([max(start1, start2), min(end1, end2)])
                if end1 > end2:
                    r += 1
                else:
                    l += 1
                
        return result
            
