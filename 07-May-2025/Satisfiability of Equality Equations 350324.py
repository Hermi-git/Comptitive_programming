# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = [i for i in range(26)]
        rank = [0 for i in range(26)]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            rankx, ranky = rank[rootx], rank[rooty]

            if rankx > ranky:
                root[rooty] = rootx
            elif rankx < ranky:
                root[rootx] = rooty
            else:
                root[rooty] = rootx
                rankx += 1
        
        for x, o1, _, y in equations:
            val1 = ord(x) - ord("a")
            val2 = ord(y) - ord("a")
            if o1 == "=":
                union(val1, val2)
        
        for x, o1, _, y in equations:
            val1 = ord(x) - ord("a")
            val2 = ord(y) - ord("a")
            if o1 == "!":
                rootx = find(val1)
                rooty = find(val2)
                if rootx == rooty:
                    return False
        return True
                    
        


