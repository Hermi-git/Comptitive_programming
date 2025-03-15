# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        l = 0
        r = len(nums)//2
        while r < len(nums):
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r += 1
        return ans
        