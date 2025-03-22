# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def subset(first, sub):
            result.append(sub[:])
            for i in range(first, len(nums)):
                sub.append(nums[i])
                subset(i+1, sub)
                sub.pop()
            return
        subset(0, [])
        return result

