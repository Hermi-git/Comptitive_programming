# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        size = max(costs) + 1
        count = [0] *size

        for cost in costs:
            count[cost] += 1
        
        target = 0
        for idx, val in enumerate(count):
            for _ in range(val):
                costs[target] = idx
                target += 1
        
        bars = 0
        for cost in costs:
            if cost <= coins:
                bars += 1
                coins -= cost
        return bars