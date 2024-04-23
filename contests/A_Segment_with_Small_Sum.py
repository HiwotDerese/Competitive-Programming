leng, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
_max, _sum, left = 0, 0, 0



for right in range(leng):
    _sum += arr[right]
    while _sum > target:
        _sum -= arr[left]
        left += 1

    _max = max(_max, right - left + 1)
print(_max)







# left = _sum = 0
# for right in range(leng):
#     _sum += arr[right]

#     while _sum > target:
#         _sum -= arr[left]
#         left += 1

#     _max = max(_max, right - left + 1)


# print(_max)



# for i in range(leng):
#     _sum = 0
#     for j in range(i, leng):
#         _sum += arr[j]

#         if _sum <= target:
#             _max = max(_max, j - i + 1)

#         else:
#             break
    

# print(_max)
    
