class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def get_primes(n, left):
            prime = [True] * (n + 1)
            p = 2
            while p ** 2 <= n:
                if prime[p]:
                    for i in range(p ** 2, n + 1, p):
                        prime[i] = False
                p += 1
            # print(prime)
            primes = []
            for i in range(2, n + 1):
                if prime[i] and i >= left:
                    primes.append(i)

            return primes

        primes = get_primes(right, left)
        # print(primes)
        n = len(primes)

        if len(primes) < 2:
            return [-1, -1]

        ans = [primes[0], primes[1]]
        min_ = primes[1] - primes[0]

        for idx in range(1, n - 1):
            diff = primes[idx + 1] - primes[idx]
            if diff < min_:
                min_ = diff
                ans = [primes[idx], primes[idx + 1]]

        return ans