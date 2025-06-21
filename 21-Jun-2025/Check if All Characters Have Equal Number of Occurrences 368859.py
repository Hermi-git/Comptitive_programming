# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count_s = Counter(s)
        compare = count_s[s[0]]
        for value in count_s.values():
            if value != compare:
                return  False
        return True
