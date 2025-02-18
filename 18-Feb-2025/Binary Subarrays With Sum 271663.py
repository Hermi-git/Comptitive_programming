# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_dict = defaultdict(int)
        sum_dict[0] = 1
        count =0
        running_sum =0 

        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - goal in sum_dict:
                count += sum_dict[running_sum-goal]
            sum_dict[running_sum] += 1
        return count