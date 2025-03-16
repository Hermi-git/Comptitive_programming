# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                char = ""
                while stack and stack[-1] != "[":
                    char = stack.pop() + char
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(num * char)
            else:
                stack.append(ch)
        return "".join(stack) 
