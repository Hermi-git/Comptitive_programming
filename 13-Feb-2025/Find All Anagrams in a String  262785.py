# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_count = Counter(s[:len(p)])
        p_count = Counter(p)
        res =[]
        if s_count == p_count:
            res.append(0)
        for r in range(len(s)-len(p)):
            s_count[s[r+len(p)]] += 1 
            s_count[s[r]] -= 1
            if s_count[s[r]] == 0:
                del s_count[s[r]]
            if s_count == p_count:
                res.append(r+1)
        return res
            
