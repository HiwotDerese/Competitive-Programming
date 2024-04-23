def combine(n, k):
        
    def backtrack(a, arr, n, k):
    
        #base case
        if len(arr) == k:
            copy = arr[::]
            ans.append(copy)
            return

        #loop through all candidates
        for i in range(a,n+1):

            #place 
            arr.append(i)

            #call recursive function
            backtrack(i+1, arr, n, k)

            #remove
            arr.pop()
    
    
    
    
    
    ans = []
    arr = []
    
    backtrack(1, arr, n, k)
    return ans

combine(3, 2)



















