# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * n
        for start, end in requests:
            prefix[start] += 1
            if end + 1 < n:
                prefix[end + 1] -= 1

        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        

        nums.sort(reverse=True)
        prefix.sort(reverse=True)

        max_sum = 0
        for i in range(n):
            max_sum = (max_sum + nums[i] * prefix[i]) % (10**9 + 7)

        return max_sum