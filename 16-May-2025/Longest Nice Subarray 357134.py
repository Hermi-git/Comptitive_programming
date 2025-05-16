# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest =1
        l =0 
        bitmask = 0
        for r in range(len(nums)):
            while (bitmask & nums[r]) != 0:
                bitmask ^= nums[l]
                l += 1
                
            bitmask |= nums[r]
            longest = max(longest, r-l+1)
        return longest
        
            


