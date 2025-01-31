# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums_str = "".join(map(str, nums))
        int_list = [int(num) for num in nums_str]
        return int_list