# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(chr for chr in s.lower() if chr.isalnum())
        s_reverse = s[::-1]
        if s != s_reverse:
            return False
        return True 