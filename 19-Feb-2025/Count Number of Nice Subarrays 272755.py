# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
      
        count_map = defaultdict(int)
        count_map[0] = 1
        running = 0
        count = 0
        for j in range(len(nums)):
            running += nums[j]
            if running - k in count_map:
                count += count_map[running - k]
            count_map[running] += 1
        return count


            

