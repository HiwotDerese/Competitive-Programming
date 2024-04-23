class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        leng = len(weights)
        low = max(weights)
        high = sum(weights)
        _min = high
        
        while low <= high:
            mid = (high + low) // 2
            i, day, count  = 0, 1, 0
            
            while i < leng:
                count += weights[i]
                if count > mid:
                    day += 1
                    count = weights[i]
                
                # if (i + 1 >= leng) or count + weights[i + 1] > mid:
                #     day += 1
                #     count = 0
                    
                i += 1

            if day <= days:
                _min = mid
                high = mid - 1
            else:
                low = mid + 1 
                
        return _min 
                
                
                
                
                    
                    
                    
                    
                
                
            
            
        