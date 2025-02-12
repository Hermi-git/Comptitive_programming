# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people) - 1
        boat =0
        people.sort()
        while left <= right:
            summ = people[left] + people[right]
            if summ <= limit:
                left += 1
            right -= 1
            boat += 1
        return boat
                