class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = prod(nums)
        factors = set()
        divisor = 2
        while divisor <= product:
            if product % divisor == 0:
                factors.add(divisor)
                product //= divisor
            else:
                divisor += 1

        # print(factors)
        return len(factors)