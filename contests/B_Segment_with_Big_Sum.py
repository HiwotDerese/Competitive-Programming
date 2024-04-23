leng, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
_min, _sum, left = float("inf"), 0, 0

for right in range(leng):
    _sum += arr[right]
    while _sum >= target:
        _min = min(_min, right - left + 1)
        _sum -= arr[left]
        left += 1

if _min == float('inf'):
    print("-1")
else: 
    print(_min)



# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
 
# left, right, currSum = 0, 0, 0
# min_length = float('inf')
 
# while right < n:
#     currSum += arr[right]
#     while currSum >= s:
#         min_length = min(min_length, right - left + 1)
#         currSum -= arr[left]
#         left += 1
#     right += 1
 
# if min_length == float('inf'):
#     print("-1")
# else:
#     print(min_length)







