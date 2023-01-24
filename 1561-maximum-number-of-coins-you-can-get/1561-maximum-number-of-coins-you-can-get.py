class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        x = sorted(piles, reverse=True)
        res = 0 
        i = 1
        while i < 2*(len(piles)/3):
            res = res + x[i]
            i += 2
        
        return res

            
        