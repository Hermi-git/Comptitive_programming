# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window= n - k
        total = sum(cardPoints)
        summ = sum(cardPoints[:window])
        cur_sum = total - summ
        max_sum = cur_sum
        for i in range(n-window):
            summ = summ + cardPoints[i+window] - cardPoints[i]
            cur_sum = total - summ
            max_sum = max(max_sum, cur_sum)
        return max_sum