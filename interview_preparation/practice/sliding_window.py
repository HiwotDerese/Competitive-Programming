# 159

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

# s = 'eceba'
# dic = {}
# ans = 0
# left = 0
# n = len(s)
# for right in range(n):
#     dic[s[right]] = dic.get(s[right], 0) + 1

#     while len(dic) > 2:
#         dic[s[left]] -= 1
#         if dic[s[left]] == 0:
#             dic.pop(s[left])
#         left += 1

#     ans = max(ans, right - left + 1)

# print(ans)



# 1100
s = 'havefunonleetcode'
k = 5
dic = {}
ans = 0
left = 0
n = len(s)
for right in range(n):
    dic[s[right]] = dic.get(s[right], 0) + 1

    while dic[s[right]] > 1 or right - left + 1 > k:
        dic[s[left]] -= 1
        left += 1

    if right - left + 1 == k:
        ans += 1

print(ans)
