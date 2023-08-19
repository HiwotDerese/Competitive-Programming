class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count=0
        for i,c in enumerate(s):
            if c==' ':
                count+=1
                if count==k:
                    return s[:i]
        return s