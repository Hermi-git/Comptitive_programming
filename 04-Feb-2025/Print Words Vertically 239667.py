# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = list(s.split(" "))
        
        max_str = max(len(ch)for ch in s_list)
        
        final = []
        for i in range(max_str):
            temp = []
            for j in range(len(s_list)):
                
                if len(s_list[j]) <= i:
                    temp.append(" ")
                else:
                    temp.append(s_list[j][i])
            final.append("".join(temp).rstrip())
        return final

 


        