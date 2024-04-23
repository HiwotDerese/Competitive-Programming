s, b = map(int, input().split())
a = list(map(int, input().split()))
sorted_ = sorted(a)
arr = []

for i in range(b):
    d, g = map(int, input().split())
    arr.append([d, g])

print(arr)

arr.sort()
dic, j, curr = {}, 0, 0
for i in range(b):
    while j < s and sorted_[j] < arr[i][0]:
        dic[sorted_[j]] = curr
        j += 1
    curr += arr[i][1]

ans = [dic[a[i]] for i in range(s)]
print(*ans)