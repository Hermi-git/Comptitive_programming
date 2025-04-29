# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mink_idx = -1
        maxk_idx = -1
        invalid_idx = -1
        count =0

        for i in range(len(nums)):
            if nums[i] == minK:
                mink_idx = i
            if nums[i] == maxK:
                maxk_idx = i
            if nums[i] < minK or nums[i] > maxK:
                invalid_idx = i
            subarray = min(mink_idx, maxk_idx) - invalid_idx
            subarrays = max(subarray, 0)
            count += subarrays
        return count

