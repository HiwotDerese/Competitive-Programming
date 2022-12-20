class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        k = 3
        st = s[:k]
        for i in range(len(s) - 2):
            if len(set(st)) == 3:
                count += 1
            st = s[i+1:k+1]
            k += 1
        return count
        
