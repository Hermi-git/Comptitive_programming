# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * n
        for first, last, seats in bookings:
            prefix[first-1] += seats
            if last < n:
                prefix[last] -= seats
        ps = list(itertools.accumulate(prefix))
        return ps
    
