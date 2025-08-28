# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        goal = ""
        for i in range(len(command)):
            if command[i] == "G":
                goal += "G"
            if command[i] == "(":
                if command[i+1].isalpha():
                    goal += "al"
                else:
                    goal += "o"
        return goal

