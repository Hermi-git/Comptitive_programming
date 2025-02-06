# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_count =Counter(nums) 
        #1:2, 3:2, 2:3
        pair = 0
        unpair = 0
        for num in nums_count:
            if nums_count[num] % 2 ==1:
                unpair += 1   
            
            pair += nums_count[num] // 2
        return [pair, unpair]
