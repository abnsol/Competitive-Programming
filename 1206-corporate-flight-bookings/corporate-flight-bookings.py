class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        rangeUpdate = [0] * (n + 1)

        for first,last,seats in bookings:
            rangeUpdate[first] += seats
            if last < n:
                rangeUpdate[last + 1] -= seats

        acc = 0
        for i in range(n):
            acc += rangeUpdate[i + 1]
            rangeUpdate[i] = acc

        return rangeUpdate[:-1]