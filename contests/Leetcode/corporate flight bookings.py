class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*n
        first = 0
        last = 0
        seat = 0
        for i in range(len(bookings)):
            first = bookings[i][0]
            last = bookings[i][1]
            seat = bookings[i][2]
            ans[last - 1] += seat
            if first > 1:
                ans[first - 2] -= seat 
        for i in range(n-2, -1,-1):
            ans[i] += ans[i+1]

        return ans