m = int(input())
arr = list(map(int, input().split()))
unique = set(arr)
ans = 1

for i in range(2, len(unique) + 1):
    ans *= i

print(ans)