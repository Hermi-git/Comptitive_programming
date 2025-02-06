# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_dict = Counter()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                prod_dict[prod] += 1
        count = 0
        for freq in prod_dict.values():
            if freq >= 2:
                count += (freq * (freq-1)//2) * 8 
        return count

