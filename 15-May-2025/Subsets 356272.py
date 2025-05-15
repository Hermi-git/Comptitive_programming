# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subset = 1 << n

        power_set = []
        for mask in range(total_subset):
            sub = []
            for i in range(n):
                if (mask & (1<<i)) != 0:
                    sub.append(nums[i])
            power_set.append(sub)
        return power_set
