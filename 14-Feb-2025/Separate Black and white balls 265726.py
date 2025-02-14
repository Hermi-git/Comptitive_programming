# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        count_zero = 0
        ans = 0
        for i in range(len(s)-1, -1, -1): 
            if s[i] == '0':
                count_zero += 1
            if s[i] =='1':
                ans += count_zero
                
        return ans
            
