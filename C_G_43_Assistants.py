test = int(input())

for _ in range(test):
    n = int(input())
    ranges, max_ = [], 0

    for _ in range(n):
        start, end = map(int, input().split())
        ranges.append((start, end))
        max_ = max(max_, end)
    
    arr = [0] * (max_ + 1)
    for i in range(len(ranges)):
        arr[ranges[i][0]] += 1
        arr[ranges[i][1]] -= 1

    for idx in range(1, max_):
        arr[idx] += arr[idx - 1]

    print(max(arr))

    


