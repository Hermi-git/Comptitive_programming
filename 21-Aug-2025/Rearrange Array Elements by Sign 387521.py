# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = [num for num in nums if num <0 ]
        positive = [num for num in nums if num > 0]

        n = p =0
        res = []
        while n < len(negative) and p < len(positive):
            res.append(positive[p])
            res.append(negative[n])
            p+=1
            n+=1
        return res 


       