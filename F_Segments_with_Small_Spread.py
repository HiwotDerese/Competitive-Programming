from collections import deque

n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

increase = deque()
decrease = deque()
count = 0
l = 0

for r in range(len(arr)):
    while increase and arr[increase[-1]] < arr[r]:
        increase.pop()
        
    increase.append(r)
    
    
    while decrease and arr[decrease[-1]] > arr[r]:
        decrease.pop()
        
    decrease.append(r)
    
    
    while arr[increase[0]] - arr[decrease[0]] > k:
        if l == increase[0]:
            increase.popleft()
            
        if l == decrease[0]:
            decrease.popleft()
            
            
        l += 1
                
            
    count = count + r - l + 1
                      
print(count)