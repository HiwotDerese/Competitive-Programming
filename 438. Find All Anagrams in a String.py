class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
            
        hash1 = OrderedDict((i,0) for i in ascii_lowercase)
        hash2 = OrderedDict((i,0) for i in ascii_lowercase)
        ans = []
        for i in range(len(p)):
            hash1[p[i]] += 1
            hash2[s[i]] += 1
        i = 0
        j = len(p)
        while j < len(s):
            if hash1 == hash2:
                ans.append(i)
            hash2[s[i]] -= 1
            if j != len(s):
                hash2[s[j]] += 1
            i += 1
            j += 1
        if hash1 == hash2:
            ans.append(i)
        return ans
            


        
        