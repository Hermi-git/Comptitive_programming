# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_count = Counter(deck)
        freq = list(deck_count.values())

        res = reduce(math.gcd, freq)
        if res >= 2:
            return True
        else:
            return False