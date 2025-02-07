# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False  
        result = []
        temp = [] 
        
        for line in source:
            i = 0
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    in_block = True  
                    i += 1  
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    in_block = False  
                    i += 1  
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break  
                elif not in_block:
                    temp.append(line[i])  
                i += 1
            
            if not in_block and temp:
                result.append("".join(temp))  
                temp = []  
        
        return result
