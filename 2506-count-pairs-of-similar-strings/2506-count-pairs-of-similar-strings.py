class Solution:
    def similarPairs(self, w: List[str]) -> int:
        cnt=0
        for i in range(len(w)):
            # print(cnt)
            for j in range(i):
                # print(i,j)
                if set(w[i])==set(w[j]):
                    cnt+=1
            print(cnt)
        return cnt