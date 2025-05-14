# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for i in nums:
            single_num ^= i
        return single_num
        