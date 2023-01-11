test = int(input())
arr = []
 
for i in range(test):
    arr.append(input())
    
leng = len(arr[0])
ans = []
 
for i in range(leng):
    char = '?'
    for j in range(test):
        curr = arr[j][i]
        if char == '?':
            char = curr
        elif curr == '?':
            continue
        elif char != curr:
            char = 'not_equal'
            break
    
    if char == 'not_equal':
        ans.append('?')
    elif char == '?':
        ans.append('c')
    else:
        ans.append(char)
 
print("".join(ans))
        



        

