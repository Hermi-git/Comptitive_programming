# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        n = len(nums)
        appear = math.floor(n/3)
        result = []
        for num in nums_count:
            if nums_count[num] > appear:
                result.append(num)
        return result