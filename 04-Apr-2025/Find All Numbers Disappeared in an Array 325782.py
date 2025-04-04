# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        result =[]
        for num in range(1,len(nums)+1):
            if num not in nums_count:
                result.append(num)
        return result