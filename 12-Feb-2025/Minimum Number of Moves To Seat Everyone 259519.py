# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        min_moves = 0
        p1 = p2 = 0 
        while p1< len(seats) and p2< len(students):
            move = abs(seats[p1] - students[p2])
            min_moves += move
            p1 += 1
            p2 += 1
        return min_moves