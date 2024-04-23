class Solution:
    
    def fairD(self, distribution, index, cookies, k):
        if index == len(cookies):
            
            return max(distribution)
        
        min_unfairness = float('inf')
        
        for i in range(k):
            
            distribution[i] += cookies[index]
            
            if distribution[i] < min_unfairness:
                min_unfairness = min(min_unfairness, self.fairD(distribution, index + 1, cookies, k))

            distribution[i] -= cookies[index]
            
        return min_unfairness

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        index, self._max, self._min = 0, -float('inf'), float('inf')
        distribution = [0] * k
        
        return self.fairD(distribution, index, sorted(cookies, reverse=True), k)
        
        
        
        
        
        
        
        
        
        
        
        