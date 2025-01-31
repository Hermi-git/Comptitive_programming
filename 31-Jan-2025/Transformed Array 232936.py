# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] > 0:
                index = (i + nums[i]) % n
            elif nums[i] < 0:
                index = (i - abs(nums[i]) + n) % n
            else:
                index = i
            result[i] = nums[index]
        return result
            


