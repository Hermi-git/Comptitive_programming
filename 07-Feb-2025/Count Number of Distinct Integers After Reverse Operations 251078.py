# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set()
        for i in range(len(nums)):
            nums_set.add(nums[i])
        for num in nums:
            num = int(str(num)[::-1])
            nums_set.add(num)
        return len(nums_set)
