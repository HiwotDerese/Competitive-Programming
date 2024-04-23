test = int(input())
arr = []
cases = list(map(lambda a: int(a), input().split()))
# unique = list(set(cases))
# print(unique)
leng = len(cases)
arr.append(cases[0])
ans = 0
for i in range(1,leng):
    
    if cases[i] not in arr:
        arr.append(cases[i])
        
        if cases[i] == min(arr) or cases[i] == max(arr):
            ans += 1
print(ans)

