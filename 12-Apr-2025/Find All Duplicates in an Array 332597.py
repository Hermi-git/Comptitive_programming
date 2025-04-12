# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                res.append(num)
            nums[num-1] = -nums[num-1]
        return res