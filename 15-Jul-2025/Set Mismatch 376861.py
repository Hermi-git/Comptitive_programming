# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        result = []
        for num in count_nums:
            if count_nums[num] == 2:
                result.append(num)
        for num in range(1, len(nums)+1):
            if num not in nums:
                result.append(num)
        return result