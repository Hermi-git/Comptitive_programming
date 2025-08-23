# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        bp = [n for n in nums if n < pivot]
        ep = [n for n in nums if n == pivot]
        ap = [n for n in nums if n > pivot]

        return bp + ep + ap