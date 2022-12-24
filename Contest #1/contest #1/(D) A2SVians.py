num = int(input())
stdnt = input().split()
# print(stdnt[0])
bad = input()
ans = 0

for i in range(num):
    if stdnt[i] in bad:
        continue
    
    else:
        unique = set(stdnt[i])
        leng = len(stdnt[i])
        if len(unique) == leng:
            ans += 1
            
print(ans)
    