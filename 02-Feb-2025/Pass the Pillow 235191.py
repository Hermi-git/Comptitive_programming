# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index, direction = 1, 1
        while time > 0:
            index += direction
            if index == n or index == 1:
                direction *= -1
            time -=1
        return index
                


