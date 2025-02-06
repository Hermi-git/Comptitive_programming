# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = Counter(nums)
        result = []
        for num in nums_dict:
            if nums_dict[num] == 2:
                result.append(num)
        return result
