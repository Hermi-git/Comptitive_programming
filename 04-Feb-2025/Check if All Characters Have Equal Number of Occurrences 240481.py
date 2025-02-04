# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_count = Counter(s)
        compare_s = s_count[s[0]]
        for value in s_count.values():
            if value != compare_s:
                return  False
        return True
