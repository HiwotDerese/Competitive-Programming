class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr, ans = 1, 0
        while n > 0:
            if n >= curr:
                ans += 1
                n -= curr
                curr += 1

            else:
                break

        return ans

        