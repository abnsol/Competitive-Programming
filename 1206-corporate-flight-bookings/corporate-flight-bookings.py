class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # range sum query
        seats = [0] * (n + 1)

        for first,last,seat in bookings:
            seats[first - 1] += seat
            seats[last] -= seat
        
        ans = [seats[0]]
        for i in range(1,n):
            ans.append(ans[i - 1] + seats[i])
        
        return ans

