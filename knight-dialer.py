class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
        mod = 1000000007

        def inbound(r, c):
            if 0 <= r < 4 and 0 <= c < 3 and (r, c) not in [(3, 0), (3, 2)] :
                return True

            return False
            
        dp = {}
        def countPhoneNumbers(r, c, l):
            if not inbound(r, c):
                return 0

            if n == l:
                return 1

            if (r, c, l) in dp:
                return dp[(r, c, l)]

            v = 0
            for r0, c0 in directions:
                v += countPhoneNumbers(
                    r + r0, c + c0, l + 1)

            dp[(r, c, l)] = v

            return dp[(r, c, l)] % mod

        res = 0
        for r in range(4):
            for c in range(3):
                res += countPhoneNumbers(r, c, 1)

        return res % mod