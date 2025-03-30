# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1] - position[0]
        ans = 0

        def can_placed(x):
            last = position[0]
            count = 1
            for i, pos in enumerate(position):
                if abs(pos - last) >= x:
                    count += 1
                    last = position[i]
            return count >= m

        while l <= r:
            mid = (l+r)//2

            if can_placed(mid):
                ans = mid
                l = mid+1
            else:
                r = mid - 1
        return ans 
                