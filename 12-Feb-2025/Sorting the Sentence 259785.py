# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = list(s.split())
        for ch in s_list:
            sort_list = sorted(s_list, key= lambda ch:ch[-1])
        modified_s = [word[:-1] for word in sort_list ]

        return " ".join(modified_s)
