# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        left = n-2
        i, max_coin = 0, 0
        while i < n/3:
            max_coin += piles[left]
            left -= 2
            i += 1
        return max_coin
        