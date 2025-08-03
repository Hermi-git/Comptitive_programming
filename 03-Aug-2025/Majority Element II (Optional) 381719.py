# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        n = len(nums)
        appear = math.floor(n/3)
        ans = []
        for num in count_nums:
            if count_nums[num] > appear:
                ans.append(num)
        return ans