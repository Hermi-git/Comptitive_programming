# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_num = set(nums)
        list_nums = list(set_num)
        list_nums.sort()
       
        if len(list_nums) >= 3:
            return list_nums[-3]
        else:
            return list_nums[-1]