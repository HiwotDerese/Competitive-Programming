class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in range(len(arr)): 
            if arr[i] not in d:   
                d[arr[i]]=1       
            else:                 
                d[arr[i]]+=1      

        l= d.values()             

        if len(set(l)) == len(l): 
            return True
        else:
            False    
