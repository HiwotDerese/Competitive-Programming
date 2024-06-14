n, k = map(int, input().split())

rules = list(map(int, input().split()))
behav = list(map(int, input().split()))

prefix = [rules[0] if behav[0] == 0 else 0] 

for i in range(1, n):
    prefix.append(prefix[i - 1] + rules[i] if behav[i] == 0 else prefix[i - 1])

left, max_ = 0, prefix[k - 1]

for right in range(k, n):
    curr = prefix[right] - prefix[left]
    max_ = max(max_, curr)
    left += 1

ans = 0
for i in range(n):
    if behav[i] == 1:
        ans += rules[i]

print(ans + max_)