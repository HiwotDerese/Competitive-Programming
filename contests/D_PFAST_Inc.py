n, m = map(int, input().split())
dic = {}

for _ in range(n):
    voluteer = input()
    dic[voluteer] = 1

for _ in range(m):
    pair1, pair2= list(input().split())
    dic[pair2] -= 1

ans = []
for i in dic:
    if dic[i] > 0:
        ans.append(i)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

