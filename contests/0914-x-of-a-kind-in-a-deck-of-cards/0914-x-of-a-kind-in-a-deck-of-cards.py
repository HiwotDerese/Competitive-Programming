class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        
        dic = {}
        for i in deck:
            dic[i] = 1 + dic.get(i, 0)
            
            
        count = set(list(dic.values()))
        
        def trial_division_simple(n: int) -> list[int]:
            factorization = set()
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.add(n)

            return factorization
    
        arr = []
        for i in count:
            # print(i)
            
            num = trial_division_simple(i)
            arr.append(num)
        
        # print(arr)
        ans = set(arr[0]).intersection(*arr)
        if ans:
            return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        