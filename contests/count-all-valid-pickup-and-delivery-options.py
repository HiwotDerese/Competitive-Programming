class Solution:
    def countOrders(self, n: int) -> int:
        prod = 1
        m = n
        m *= 2
        mod = 10**9 + 7
        fac = math.factorial(2*n)

        return (fac//pow(2, n)) % mod