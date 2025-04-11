# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in trust:
            adj_list[u].append(v)
        for person in range(1, n+1):
            if person not in adj_list:
                c = 0
                for node in range(1, n + 1):
                    if person in adj_list[node]:
                        c += 1
                if c== n-1:
                    return person
        return -1