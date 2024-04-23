test = int(input())

for _ in range(test):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans, curr, sum_ = 0, 1, 0

    while ans + sum_ <= x:
        ans += sum_

        sum_ = 0
        for i in range(n):
            if arr[i] == curr:
                sum_ += 1
                arr[i] += 1

        curr += 1

    print(curr - 1)



# sum_ = 0


