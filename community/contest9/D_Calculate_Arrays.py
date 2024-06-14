n = int(input())
arr = list(map(int, input().split()))

xi = 0
for b in arr:
    print(b + xi, end = ' ')
    xi += max(0, b)

