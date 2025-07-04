# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = [num for num in nums if num <0 ]
        pos = [num for num in nums if num > 0]

        n = p =0
        ans = []
        while n < len(neg) and p < len(pos):
            ans.append(pos[p])
            ans.append(neg[n])
            p+=1
            n+=1
        return ans 


       