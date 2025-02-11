# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size = max(nums) +1
        count = [0] * size
        for num in nums:
            count[num] += 1
        j = 0
        for idx, val in enumerate(count):
            for _ in range(val):
                nums[j] = idx
                j += 1
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res