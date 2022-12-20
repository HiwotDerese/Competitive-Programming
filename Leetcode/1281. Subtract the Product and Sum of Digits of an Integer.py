class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums = 0
        prod = 1
        for i in str(n):
            print(i)
            sums += int(i)
            prod *= int(i)
        return prod - sums
