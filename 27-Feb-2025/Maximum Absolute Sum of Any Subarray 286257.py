# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_head = 0
        max_sum = 0
        for i in range(len(nums)):
            max_head = max(max_head + nums[i], nums[i])
            max_sum = max(max_sum, max_head)
        min_head = 0
        min_sum = 0
        for i in range(len(nums)):
            min_head = min(min_head + nums[i], nums[i])
            min_sum = min(min_sum, min_head)
        
        result = max(max_sum, abs(min_sum))
        return result