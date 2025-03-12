# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        queue = deque(range(n))  
        revealed_order = [] 

        while queue:
            revealed_order.append(queue.popleft())
            if queue:
                queue.append(queue.popleft())

        deck.sort()
        answer = [0] * n 
        for i in range(n):
            answer[revealed_order[i]] = deck[i]
        return answer

        
