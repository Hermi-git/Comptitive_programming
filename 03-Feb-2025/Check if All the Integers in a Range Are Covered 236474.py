# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range(left, right+1):
            iscovered = False
            for start, end in ranges:
                if start <= i <= end:
                    iscovered = True
                    break
            if not iscovered:
                return False
        return True
                

