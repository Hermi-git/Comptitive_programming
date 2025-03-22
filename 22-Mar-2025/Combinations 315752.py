# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(firstnum, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for cand in range(firstnum, n+1):
                path.append(cand)
                backtrack(cand+1, path)
                path.pop()


        backtrack(1, [])
        return ans

        