# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) -1
        res = []
        while l <= r:
            if nums[l]**2 < nums[r]**2:
                res.append(nums[r]**2)
                r -= 1
            else:
                res.append(nums[l]**2)
                l += 1
        return res[::-1]
