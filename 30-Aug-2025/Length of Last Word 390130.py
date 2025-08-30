# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_s = s.strip()
        list_s = list(cleaned_s.split(' '))
      
        last_word = list_s[-1]
        return len(last_word)