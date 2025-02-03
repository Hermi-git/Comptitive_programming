# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in nums_dict:
                return [index, nums_dict[difference]]
            nums_dict[value] = index




    
                
                
                  


