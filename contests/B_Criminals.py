test = int(input())

for i in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0

    for i in range(n-2):
        if nums[i] > 0 and nums[i+1] == 0:
            nums[i] -= 1
            nums[i + 1] += 1
            count += 1

    add = sum(nums[:n-1])
    count += add
    print(count)


    