# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0 
        r = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[-1] > nums[mid]:
                r = mid-1
            if nums[-1] < nums[mid]:
                l = mid + 1
