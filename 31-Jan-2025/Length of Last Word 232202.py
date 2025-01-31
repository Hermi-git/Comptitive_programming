# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_clean = s.strip()
        s_list = list(s_clean.split(' '))
        print(s_list)
        last_length = len(s_list[-1])
        return last_length