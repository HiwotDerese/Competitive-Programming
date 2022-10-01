class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 0:
            return 0
        ans = 1
        i = 0
        j = 0
        hash = {}
        n = len(fruits)
        minm = 0
        while j < n:
            if len(hash) <= 2:
                hash[fruits[j]] = j 
                j += 1
            if len(hash) > 2:
                minm = n - 1
                for i in hash.values():
                    minm = min(minm, i)
                i = minm + 1
                hash.pop(fruits[minm])
            ans = max(ans, j - i)
        return ans

