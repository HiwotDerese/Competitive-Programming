def combine(n: int, k: int):
        
    def backtrack(num, candidate, k, ans):
        
        if len(candidate) == k - 1:
            comb = candidate
            comb.insert(0, num)
            # print('aaaaa')
            ans.append(comb)
            # print(ans)
            return 
            
            
        for i in range(len(candidate)):
            ans.append()
            print(candidate, 'candidate', num)
            if len(candidate) >= k:
                backtrack(candidate[i], candidate[i+1:], k, ans)
                
                
    
    ans = []
    arr = []
    
    for i in range(n):
        arr.append(i + 1)
        
    backtrack(arr[0], arr[1:], k, [])
    
    return ans

combine(4, 2)