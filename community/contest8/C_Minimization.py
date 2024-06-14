n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
    for _ in range(k - 1):
        print(0)

    exit()

a.sort()
non_zeros = 0

for i in range(n - 1):
    if non_zeros == 0 and a[i] != 0:
        print(a[i])
        non_zeros += 1
        if non_zeros == k:
            break
    if non_zeros > 0:
        if a[i + 1] > a[i]:
            print(abs(a[i + 1] - a[i]))
            non_zeros += 1

    if non_zeros == k:
        break

for _ in range(k - (non_zeros)):
    print(0)
    