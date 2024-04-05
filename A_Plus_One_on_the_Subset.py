test = int(input())

for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1] - a[0])