n, a, b = list(map(int, input().split()))
problems = list(map(int, input().split()))
_sum, ans, left, count = 0, 0, 0, 0
 
for right in range(n):
    # print(left, right)
    _sum += problems[right]
 
    while _sum >= a:
        _sum -= problems[left]
        left += 1

    count += (right - left + 1)

 

count2, _sum, left = 0, 0, 0
for right in range(n):
    # print(left, right)
    _sum += problems[right]
 
    while _sum > b:
        _sum -= problems[left]
        left += 1

    count2 += (right - left + 1)

print(count2 - count)



