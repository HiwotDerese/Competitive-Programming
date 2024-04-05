test = int(input())
for i in range(test):
    s = input()
    n = len(set(s))
    if n == 1:
        print(-1)
    else:
        print(len(s) - 1)