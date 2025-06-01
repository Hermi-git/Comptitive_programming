# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        l=r=0
        while l < len(word1) and r < len(word2):
            answer += word1[l]
            answer  += word2[r]
            l += 1
            r += 1
        while r < len(word2):
            answer += word2[r]
            r += 1
        while l < len(word1):
            answer += word1[l]
            l += 1
        return answer