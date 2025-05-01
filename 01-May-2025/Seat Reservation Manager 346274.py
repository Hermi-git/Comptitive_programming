# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.seats = n
        self.min_heap = []
        for num in range(1, n+1):
            heapq.heappush(self.min_heap, num)
        

    def reserve(self) -> int:
        return heapq.heappop(self.min_heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.min_heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)