# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_count = Counter(s2[:len(s1)])
        s1_count = Counter(s1)
        if s1_count == s2_count:
            return True
        for i in range(len(s2) - len(s1)):
            s2_count[s2[i+len(s1)]] += 1
            s2_count[s2[i]] -= 1
            if s2_count[s2[i]] == 0:
                del s2_count[s2[i]]
            if s1_count == s2_count:
                return True 
        return False
        
                
        