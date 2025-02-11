# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_val = max(nums) 
        min_val = min(nums)
        size = max_val - min_val +1 
        count = [0] * size

        for num in nums:
            count[num-min_val] += 1
        
        target = 0
        for idx, val in enumerate(count):
            for i in range(val):
                nums[target] = idx + min_val
                target += 1
        
        return nums