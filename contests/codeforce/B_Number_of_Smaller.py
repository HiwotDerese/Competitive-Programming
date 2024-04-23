m,n = list(map(int, input().split()))

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ans = []
count = 0

i = 0
j = 0

while j < n:
    if list1[i] < list2[j]:
        count += 1
        i += 1
        if i == m:
            while j < n:
                ans.append(count)
                j += 1
    else:
        ans.append(count)
        j += 1
        

print(*ans)
