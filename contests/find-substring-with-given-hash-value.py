class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        val = {}
        for i in range(97, 123):
            val[chr(i)] = i - 96

        left, n = 0, len(s)
        # dic_ = {}
        # for idx in range(k):
        #     dic_[idx] = pow(power, idx)


        window = 0
        power_base = 1
        for idx in range(k):
            window += val[s[idx]] * power_base
            power_base *= power

        left = 0

        if window % modulo == hashValue:
            return s[left:k] 

        new_multiplier = power ** (k-1)
        for right in range(k, n):
            window -= val[s[left]]
            window //= power
            window += val[s[right]] * new_multiplier
            left += 1

            if window % modulo == hashValue:
                return s[left:right + 1]