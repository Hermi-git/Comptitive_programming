# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = sum(1 for c in s if c.isalpha()) 
        total_permutation = 1 << n  
        result = []

        for mask in range(total_permutation):
            sub = ""
            letter_index = 0  
            for c in s:
                if c.isalpha():
                    if (mask >> letter_index) & 1:
                        sub += c.upper()
                    else:
                        sub += c.lower()
                    letter_index += 1
                else:
                    sub += c  
            result.append(sub)

        return result
