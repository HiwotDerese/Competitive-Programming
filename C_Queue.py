# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# time, ans = [0]*n, 0

# for i in range(1, n):
#     time[i] = arr[i - 1] + time[i - 1]
#     if time[i] <= arr[i]:
#         ans += 1

# print(ans + 1)



n = int(input())
arr = list(map(int, input().split()))
arr.sort()
time, ans = [0] * n, 0

for i in range(1, n):
    time[i] = arr[i - 1] + time[i - 1]

for i in range(n):
    if time[i] <= arr[i]:
        ans += 1

print(ans)



# n = int(input())
#     time = sorted(map(int, input().split()))

#     ans = waitTime = 0
#     for i in range(n):
#         if waitTime <= time[i]:
#             ans += 1
#             waitTime += time[i]
    
#     print(ans)