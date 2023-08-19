num = list(map(int, input().strip()))
# print(num)
ans = 0

n = len(num)

def rec(idx):
    if idx >= n:
        return
    if sum(num[left:right]) % 3 == 0:
        ans += 1

    for right in range(left + 1, n):
        rec(right)
    

for left in range(len(num)):
    right = left
    rec(left)

print(ans)











