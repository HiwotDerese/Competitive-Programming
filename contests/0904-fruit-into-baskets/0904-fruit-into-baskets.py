class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        leng = len(fruits)
        left, right, _max, index = 0, 0, 0, []
        trees = []
        
        while right < leng:
            
            while right < leng and len(trees) <= 2:
                if len(trees) < 2:
                    if fruits[right] not in trees:
                        trees.append(fruits[right])
                        # index.append(right)
                        right += 1
                    else:
                        right += 1
                        
                else:
                    if fruits[right] in trees:
                        right += 1
                    else:
                        break
            
            _max = max(_max, right-left)
            print(_max, left, right)
            left = right - 1
            while left > 0 and nums[left] == nums[left - 1]:
                left -= 1
            
            trees = [fruits[left]]
        return _max
                        
                


    
    
    
    
    
    
    
    
    
    
    
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 0:
            return 0
        ans = 1
        i = 0
        j = 0
        hash = {}
        n = len(fruits)
        minm = 0
        while j < n:
            if len(hash) <= 2:
                hash[fruits[j]] = j 
                j += 1
            if len(hash) > 2:
                minm = n - 1
                for i in hash.values():
                    minm = min(minm, i)
                i = minm + 1
                hash.pop(fruits[minm])
            ans = max(ans, j - i)
        return ans


            
            