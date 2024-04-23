n, k = map(int, input().split())
s = input()

dic = {}

for i in s:
    dic[i] = 0
    
left, ans = 0, 0

for right in range(n):
    dic[s[right]] += 1
    
    while (right - left + 1) - (max(dic.values())) > k:
        dic[s[left]] -= 1
        left += 1
        
    ans = max(ans, right - left + 1)
    
    
print(ans)




