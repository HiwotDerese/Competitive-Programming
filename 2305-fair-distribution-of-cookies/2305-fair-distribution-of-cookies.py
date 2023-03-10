class Solution:
    
    def fairD(self, distribution, index, cookies, k):
        
        # print(distribution, index)
        if index == len(cookies):
            return max(distribution)
        
        min_unfairness = float('inf')
        for i in range(k):
            
            distribution[i] += cookies[index]
            
            if distribution[i] < min_unfairness:
                min_unfairness = min(min_unfairness, self.fairD(distribution, index + 1, cookies, k))
            
            # print(distribution)
            # self._max = max(self._max, )
            # return self._max
            # print(self._max, "max")
            # self._min = min(self._min, self._max)
            # print(self._min , "min")
            
            # print(i, distribution[i])
            distribution[i] -= cookies[index]
            
        return min_unfairness
            
            # return self._min
            

            # for j in range(1, k):
            #     distribution[j] += cookies[i - 1]
            #     self.fairD(distribution, index, cookies, k)
                
        # return _min
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        index, self._max, self._min = 0, -float('inf'), float('inf')
        distribution = [0] * k
        # print(distribution)
        cookies.sort()
        return self.fairD(distribution, index, cookies, k)
        
        
        
        
        
        
        
        
        
        
        
        