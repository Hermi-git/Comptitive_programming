# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # making valid pairs to identify them
        valid_pairs = {")": "(", "}":"{", "]":"["}
        for bracket in s:
            # if the brackets are open, add them to the stack
            if bracket in valid_pairs.values():
                stack.append(bracket)
            else:
                # if the bracket is closing, we need to have opening pair on the stack
                if len(stack) != 0 and stack[-1] == valid_pairs[bracket]:
                    stack.pop()
                else:
                    return False
                    # check if the opening bracket left 
        return len(stack) ==0
    
                    
        
        