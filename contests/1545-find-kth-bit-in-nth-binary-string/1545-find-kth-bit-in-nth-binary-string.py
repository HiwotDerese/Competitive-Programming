class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s):
            inverted = ""
            for i in range(len(s)):
                if s[i] == '1':
                    inverted += '0'
                else:
                    inverted += '1'

            return inverted


        def findBit(n) -> str:
            if n == 1:
                return "0"
            s = findBit(n - 1)
            return s + "1" + invert(s)[::-1]

        return findBit(n)[k-1]
        