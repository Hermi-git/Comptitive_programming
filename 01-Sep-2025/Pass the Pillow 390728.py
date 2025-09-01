# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        idx, dirn = 1, 1
        while time > 0:
            idx += dirn
            if idx == n or idx == 1:
                dirn *= -1
            time -=1
        return idx
                


