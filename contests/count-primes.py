class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [1] * (n)
        primes[0], primes[1] = 0, 0

        for idx in range(1, n):
            if primes[idx]:
                not_prime = idx * 2

                while not_prime < n:
                    if primes[not_prime]:
                        primes[not_prime] = 0

                    not_prime += idx

        return sum(primes)