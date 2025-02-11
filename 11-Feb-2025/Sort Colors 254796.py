# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] +=1 
        
        target = 0
        for idx, val in enumerate(count):
            for _ in range(val):
                nums[target] = idx
                target += 1
        return nums