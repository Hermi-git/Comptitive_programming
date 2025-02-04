# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        result = []
        for num in nums:
            if count_nums[num] == 2 and num not in result:
                result.append(num)
        return result