# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(curr_nums):
            if len(curr_nums) == len(nums):
                ans.append(curr_nums[:])
                return
            
            for num in nums:
                if num not in curr_nums:
                    curr_nums.append(num)
                    backtrack(curr_nums)
                    curr_nums.pop()
            return

        backtrack([])
        return ans