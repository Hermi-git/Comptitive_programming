# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        lst = list(s.split(" "))
        
        max_string = max(len(ch)for ch in lst)
        
        final = []
        for i in range(max_string):
            temp = []
            for j in range(len(lst)):  
                if len(lst[j]) <= i:
                    temp.append(" ")
                else:
                    temp.append(lst[j][i])
            final.append("".join(temp).rstrip())
        return final

 


        