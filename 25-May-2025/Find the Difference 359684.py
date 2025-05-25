# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_bit = 0
        t_bit = 0 

        for i in range(len(s)):
            s_bit ^= ord(s[i])
        for j in range(len(t)):
            t_bit ^= ord(t[j])
        return chr(s_bit ^ t_bit)