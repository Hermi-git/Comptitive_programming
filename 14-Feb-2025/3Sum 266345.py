# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l< r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif summ < 0 :
                    l += 1
                else:
                    r -= 1
        return result

                