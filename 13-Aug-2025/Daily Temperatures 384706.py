# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
          
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                val = i - index
                result[index] = val
            stack.append(i)
        return result
            

         