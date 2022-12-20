class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        qu = []
        index = -1
        for i in range(1,n+1):
            qu.append(i)
        while len(qu) > 1:
            index = (index + k) % len(qu)
            qu.pop(index)
            index -= 1
        return qu[0]
        
                