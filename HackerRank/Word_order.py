# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = []
ans = {}
occ = ""

for i in range(n):
    arr.append(input())
    if arr[i] in ans.keys():
        ans[arr[i]] += 1
    else:
        ans[arr[i]] = 1
print(len(ans))

for x in ans:
    print(ans[x], end=' ')

