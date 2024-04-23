class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0 and n >= 2:
            return n
        else:
            return n * 2
        