dimension = int(input())

ai, aj = list(map(int, input().split()))
bi, bj = list(map(int, input().split()))
ci, cj = list(map(int, input().split()))

flag = 0

if (bi < ai and ci < ai) or (bi > ai and ci > ai):
    if (bj < aj and cj < aj) or (bj > aj and cj > aj):
        print("YES")
    else:
        flag = 1
else:
    flag = 1

if flag == 1:
    print("NO")