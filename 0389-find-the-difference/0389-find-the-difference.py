class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1 = Counter(s)
        dic2 = Counter(t)
        for i in t:
            if i not in s:
                return i
            elif dic2[i] > dic1[i]:
                return i
            
            