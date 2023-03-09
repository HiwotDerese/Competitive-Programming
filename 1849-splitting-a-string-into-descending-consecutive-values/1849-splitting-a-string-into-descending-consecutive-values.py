class Solution:
    def splitString(self, s: str) -> bool:
        
        def split(comb, num, start, end):
        # print(comb,num,end)
        # print(comb)
            if num >= comb:
                # print(comb,num,end)
                return
            if comb - num == 1:
                # print(comb, num)

                if (end == len(s) - 1):
                    # print(comb, num)
                    return True
                if num == 0:
                    return split(comb, int(s[start:end + 2]), start, end+1)

                return split(num, int(s[end + 1]),end + 1, end + 1)

            if end >= len(s) - 1:
                # print(comb,num,end)
                return 

            # print(end)
            if end < len(s) - 2:
                # print(comb,num,end)

                return split(comb, int(s[start:end + 2]), start, end+1)
            else:   
                # print(comb,num,end)
                # print(s[end:])
                return split(comb, int(s[start:]),start, end+1)
        
    # comb = []
        for i in range(len(s) - 1):
            # print(s[:i + 1])
            if split(int(s[:i+1]), int(s[i + 1]), i + 1, i + 1):
                return True
        