# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = Counter()
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ == k:
                count += 1
            if summ - k in sum_count:
                count += sum_count[summ-k]
            sum_count[summ] += 1
        return count