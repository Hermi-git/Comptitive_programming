# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        def customSort(item1, item2):
            if item1 + item2 > item2 + item1:
                return -1  
            elif item1 + item2 < item2 + item1:
                return 1
            else:
                return 0
        
        n = len(str_nums)
        for i in range(n):
            for j in range(n - 1 - i):
                if customSort(str_nums[j], str_nums[j + 1]) == 1 :
                    str_nums[j], str_nums[j + 1] = str_nums[j + 1], str_nums[j]
        
        result = ''.join(str_nums)
        return '0' if result[0] == '0' else result