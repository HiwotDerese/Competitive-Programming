cases = int(input())
ans = 0
 
for i in range(cases):
    curr = input().split()
    leng = int(curr[0])
    curr_light = curr[1]
    
    light = input()
    light += light
    
    prev = float('inf')
    
    for i in range(2*leng):
        if light[i] == curr_light and prev == float('inf'):
            prev = i
            
        if light[i] == 'g' and prev != float('inf'):
            ans = max(ans, i - prev)
            prev = float('inf')
            
    print(ans)
    ans = 0