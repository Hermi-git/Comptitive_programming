# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            new = empty // numExchange
            total_drunk += new
            empty = new + empty % numExchange
        
        return total_drunk