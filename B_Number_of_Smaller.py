m,n = list(map(int, input().split()))

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ans = []

i = 0
j = 0

while j < len(n):
    if i == m:
        ans.append(i)
    else:
        if list1[i] < list2[j]:
            i += 1
        else:
            ans.append(i)
            i += 1
            j += 1

