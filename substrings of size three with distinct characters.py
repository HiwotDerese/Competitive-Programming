def countGoodSubstrings(self, s: str) -> int:
        i=0
        j=2
        c=0
        while j<len(s):
            if len(set(s[i:j+1]))==3:
                c+=1
            i+=1
            j=i+2
        return c