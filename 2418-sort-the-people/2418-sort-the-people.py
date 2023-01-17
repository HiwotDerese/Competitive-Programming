class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        leng = len(names)
        
        for i in range(leng):
            _max = heights[i]
            for j in range(i+1,leng):
                if _max < heights[j]:
                    _max = heights[j]
            idx = heights.index(_max)      
            names[i], names[idx] = names[idx], names[i]
            heights[i], heights[idx] = heights[idx], heights[i]
            
        return names
                
                

        
