# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before_pivot = [num for num in nums if num < pivot]
        equal_pivot = [num for num in nums if num == pivot]
        after_pivot = [num for num in nums if num > pivot]

        return before_pivot + equal_pivot + after_pivot