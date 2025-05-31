# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        sent = sorted(s_list, key = lambda word:int(word[-1]))
        res = []
        for word in sent:
            new_word = ""
            for ch in word:
                if not ch.isdigit():
                    new_word += ch
            res.append(new_word)
            
        return " ".join(res)