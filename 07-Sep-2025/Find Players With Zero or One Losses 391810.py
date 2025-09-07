# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss=[]
        one_loss=[]
        winner=Counter(match[0] for match in matches)
        losser=Counter(match[1]for match in matches)
        for i in winner:
            if i not in losser:
                zero_loss.append(i)
        for j in losser:
            if losser[j]==1:
                one_loss.append(j)
        
        zero_loss.sort()
        one_loss.sort()
        return[zero_loss,one_loss]
