# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert ="".join(str(ord(char)-96)for char in s)
        
        for _ in range(k):
            transform = sum(int(digit) for digit in convert)
            convert = str(transform)
        return transform