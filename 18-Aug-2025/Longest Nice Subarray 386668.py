# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        long =1
        l =0 
        bit_mask = 0
        for r in range(len(nums)):
            while (bit_mask & nums[r]) != 0:
                bit_mask ^= nums[l]
                l += 1
                
            bit_mask |= nums[r]
            long = max(long, r-l+1)
        return long
        
            


