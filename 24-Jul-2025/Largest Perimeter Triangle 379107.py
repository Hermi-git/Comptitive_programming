# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        for i in range(n-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                res = nums[i] + nums[i+1] + nums[i+2]
                return res
        return 0