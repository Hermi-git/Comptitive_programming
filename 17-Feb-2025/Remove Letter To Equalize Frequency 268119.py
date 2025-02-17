# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            sub = word[:i] + word[i+1:]
            word_count = Counter(sub) 
            if len(set(word_count.values())) == 1:  
                return True
        return False