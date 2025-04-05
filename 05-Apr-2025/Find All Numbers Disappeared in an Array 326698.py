# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num)-1
            nums[idx] = -1 * abs(nums[idx])
        res = []
        for i, num in enumerate(nums):
            if num>0:
                res.append(i+1)
        return res