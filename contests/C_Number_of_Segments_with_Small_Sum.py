leng, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
_max = 0

left = _sum = 0
for right in range(leng):
    _sum += arr[right]

    while _sum > target:
        _sum -= arr[left]
        left += 1

    _max += right - left + 1


print(_max)