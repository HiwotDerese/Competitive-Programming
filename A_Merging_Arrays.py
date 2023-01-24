n, m =  list(map(int, input().split()))

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ans = []

l = 0
r = 0

while l < n or r < m:
    op1 = list1[l] if l < n else float('inf')
    op2 = list2[r] if r < m else float('inf')
    if op1 < op2:
        ans.append(list1[l])
        l += 1
    else:
        ans.append(list2[r])
        r += 1

print(*ans)


