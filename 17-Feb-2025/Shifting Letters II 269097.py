# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        for shift in shifts:
            left, right, dirn = shift
            if dirn == 0:
                prefix[left] += -1
                if right + 1 < len(s):
                    prefix[right+1] += 1
            if dirn == 1:
                prefix[left] += 1
                if right + 1 < len(s):
                    prefix[right+1] += -1
        for j in range(1, len(prefix)):
            prefix[j] += prefix[j-1]
        

        ans = ""
        for k in range(len(s)):
            letter = chr(((ord(s[k]) + prefix[k] - ord('a'))% 26) + ord('a'))
            ans += letter
        return ans




            