class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """

        dp = {}
        def rec(a, b):
            if (a, b) in dp:
                return dp[(a, b)]

            if a <= 0 and b > 0:
                return 1

            if a <= 0 and b <= 0:
                return 0.5

            if a > 0 and b <= 0:
                return 0

            operation1 = rec(a - 100, b)
            operation2 = rec(a - 75, b - 25)
            operation3 = rec(a - 50, b - 50)
            operation4 = rec(a - 25, b - 75)

            dp[(a, b)] = 0.25 * (operation1 + operation2 + operation3 + operation4)

            return dp[(a, b)]

        if n >= 4800:
            return 1

        return rec(n, n)
