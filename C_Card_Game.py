n = int(input())

mati = list(map(int, input().split()))
ibsa = list(map(int, input().split()))

mati.sort()
ibsa.sort()

ans1, ans2 = 0, 0
for i in range(n):
    if mati[i] > ibsa[i]:
        ans1 += 1
    
    else:
        ans2 += 1

if ans2 >= ans1:
    print("YES")

else:
    print("NO")





