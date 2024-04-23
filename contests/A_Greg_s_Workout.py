n = int(input())

dic = {}
arr = list(map(int, input().split()))
for i in range(n):
    idx = i % 3
    if idx not in dic:
        dic[idx] = arr[i]
    else:
        dic[idx] += arr[i]

ans = float('-inf')
for i in range(len(dic)):
    if dic[i] > ans:
        max_ = i
        ans = dic[i]

if max_ == 0:
    print("chest")
elif max_ == 1:
    print("biceps")
else:    
    print("back")