n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
sorted_ = sorted(q)

end, j = 0, 0
ans = {}
for i in range(n):
    end += a[i]

    while j < m and sorted_[j] <= end:
        ans[sorted_[j]] = i + 1
        j += 1

for i in range(m):
    print(ans[q[i]])