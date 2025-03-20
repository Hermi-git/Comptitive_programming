# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        fair = float("inf")
        def fairtrack(child, i):
            nonlocal fair
            if i == len(cookies):
                fair = min(fair, max(children))
                return
            for j in range(k):
                if children[j] + cookies[i] <= fair:
                    children[j] += cookies[i]
                    fairtrack(children, i+1)
                    children[j] -= cookies[i]
        fairtrack(children, 0)
        return fair

                

