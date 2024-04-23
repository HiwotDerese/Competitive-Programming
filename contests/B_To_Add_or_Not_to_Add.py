from collections import defaultdict


n, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
ans = 0
sum_ = 0
count = 0
a = ""
dic = defaultdict(int)

for i in range(n):
    dic[nums[i]] += 1

for i in range(n):
    if dic[nums[i]] > ans:
        ans = dic[nums[i]]
        a = nums[i]


for i in range(len(nums)):
    sum_ += nums[i]
    while sum_ + k < nums[i] * (i - count + 1):
        sum_ -= nums[count]
        count += 1
    if i - count + 1 > ans:
        a = nums[i]

    ans = max(ans, i - count + 1)

print(ans, a)
