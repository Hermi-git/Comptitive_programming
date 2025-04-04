# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        result = []
        for num in nums_count:
            if nums_count[num] == 2:
                result.append(num)
        for num in range(1, len(nums)+1):
            if num not in nums:
                result.append(num)
        return result