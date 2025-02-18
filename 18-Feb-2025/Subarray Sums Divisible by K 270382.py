# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        nums_dict = defaultdict(int)
        nums_dict[0] = 1
        running =0 
        count = 0

        for i in range(len(nums)):
            running += nums[i]
            remainder = running % k
            if remainder in nums_dict:
                count += nums_dict[remainder]
            nums_dict[remainder] += 1
        return count