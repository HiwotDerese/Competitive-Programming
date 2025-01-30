n, k = map(int, input().split())
s = input()

dic = {}

for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

if len(dic) < k:
    print(0)

else:
    min_ = min(dic.values())
    print(min_ * k)