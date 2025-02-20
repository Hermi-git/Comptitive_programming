# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        for start, end, direction in shifts:
            if direction == 0:
                prefix[start] += -1
                if end+1 < len(s):
                    prefix[end+1] += 1
            if direction == 1:
                prefix[start] +=1
                if end+1 < len(s):
                    prefix[end+1] += -1
        for j in range(1,len(prefix)):
            prefix[j] += prefix[j-1]
        ans = ""
        for i in range(len(s)):
            letter = chr(((ord(s[i]) + prefix[i] - ord('a'))% 26) + ord('a'))
            ans += letter
        return ans