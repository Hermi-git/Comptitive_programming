# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_dict = defaultdict(int)
        sum_dict[0] = 1
        subarrays =0
        running =0 

        for i in range(len(nums)):
            running += nums[i]
            if running - goal in sum_dict:
                subarrays += sum_dict[running-goal]
            sum_dict[running] += 1
        return subarrays