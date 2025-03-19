# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(firstNum, path):
            if len(path) == k:
                ans.append(path[:])
                return
            if firstNum > n:
                return
            # pick the current number
            path.append(firstNum)
            backtrack(firstNum+1, path)
            path.pop()
            # not pick
            backtrack(firstNum+1, path)
        backtrack(1, [])
        return ans