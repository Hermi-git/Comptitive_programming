# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

def interpret(command) :
        res = ""
        for i in range(len(command)):
            if command[i] == "G":
                res += "G"
            if command[i] == "(":
                if command[i+1].isalpha():
                    res += "al"
                else:
                    res += "o"
        return res
command = "G()()()()(al)"
print(interpret(command))
