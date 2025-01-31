# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

def finalValueAfterOperations(operations):
        x = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                x -= 1
            if operation == "++X" or operation == "X++":
                x += 1
        return x
operations = ["--X","X++","X++"]
print(finalValueAfterOperations(operations))