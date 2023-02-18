test = int(input())

for i in range(test):
    leng = int(input())
    arr = list(map(int, input().split()))
    addi = []
    ans = []

    for i in range(leng // 2):
        ans.append(str(arr[i]))
        ans.append(str(arr[-(i+1)]))
        idx = i
    if leng % 2 != 0:
        ans.append(str(arr[idx]))
    print(" ".join(ans))