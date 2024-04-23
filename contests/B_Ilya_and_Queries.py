s = input()
m = int(input())
n = len(s)
arr = [0]*n

for i in range(n):
    if i != 0:
        arr[i] = arr[i-1] + 1 if s[i] == s[i-1] else arr[i-1]


for i in range(m):
    l, r = map(int, input().split())
    count = arr[r-1] - arr[l-1]
    print(count)

