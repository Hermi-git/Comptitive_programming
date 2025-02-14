# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        count_zero = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_zero += 1
            
            while count_zero > k:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
            max_ones = max(max_ones, r-l+1)
        return max_ones