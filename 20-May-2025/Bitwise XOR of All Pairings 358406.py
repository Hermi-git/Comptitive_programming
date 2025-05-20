# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        for a in nums1:
            xor1 ^= a
        xor2 = 0
        for b in nums2:
            xor2 ^= b

        res = 0
       
        if len(nums2) & 1:
            res ^= xor1
        
        if len(nums1) & 1:
            res ^= xor2
        return res