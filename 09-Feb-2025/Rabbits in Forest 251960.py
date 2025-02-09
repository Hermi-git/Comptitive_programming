# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbit_count = Counter(answers)
        min_rabbits = 0
        for color in rabbit_count:
            group = ceil((rabbit_count[color])/(color+1))
            ans = group * (color + 1)
            min_rabbits += ans
        return min_rabbits
