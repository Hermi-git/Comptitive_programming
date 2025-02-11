# Problem: Largest Number - https://leetcode.com/problems/largest-number/

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        def customSort(item1, item2):
            if item1 + item2 > item2 + item1:
                return -1  
            else:
                return 1   

        
        str_nums.sort(key=cmp_to_key(customSort))
        if str_nums[0] == '0':
            return '0'
        return "".join(str_nums)