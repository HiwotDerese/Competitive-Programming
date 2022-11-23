class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ["a","e","i","o","u"]
        l = 0
        r = k
        maxm = 0
        count = 0
        subs = s[:k]
        while l < k:
            if s[l] in vowel:
                count += 1
            l += 1
        maxm = count 
        l = 0
        while r < len(s):
            if k == 1 and s[l+1] in vowel:
                maxm += 1
                break
            if s[l] in vowel and count > 0:
                count -= 1
            if s[r] in vowel:
                count += 1
            l += 1
            r += 1
            maxm = max(maxm,count)
        return maxm
   
            


            





