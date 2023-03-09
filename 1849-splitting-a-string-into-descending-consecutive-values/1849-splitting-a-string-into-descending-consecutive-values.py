class Solution:
    def splitString(self, s: str) -> bool:
        
        def split(comb, num, start, end):

            if num >= comb:
                return
            if comb - num == 1:

                if (end == len(s) - 1):
                    return True
                if num == 0:
                    return split(comb, int(s[start:end + 2]), start, end+1)

                return split(num, int(s[end + 1]),end + 1, end + 1)

            if end >= len(s) - 1:
                return 

            if end < len(s) - 2:
                return split(comb, int(s[start:end + 2]), start, end+1)
            else:   
                return split(comb, int(s[start:]),start, end+1)
        
        for i in range(len(s) - 1):
            if split(int(s[:i+1]), int(s[i + 1]), i + 1, i + 1):
                return True
        