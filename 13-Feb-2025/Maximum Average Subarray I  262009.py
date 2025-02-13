# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        max_sum = summ
        for i in range(k, len(nums)):
            summ = summ + nums[i] - nums[i-k]
            max_sum = max(max_sum, summ)
        max_ave= max_sum/k
        return max_ave