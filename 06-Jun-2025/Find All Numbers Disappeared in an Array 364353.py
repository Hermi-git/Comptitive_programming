# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            val = abs(num)-1
            nums[val] = -1 * abs(nums[val])
        ans = []
        for i, num in enumerate(nums):
            if num>0:
                ans.append(i+1)
        return ans