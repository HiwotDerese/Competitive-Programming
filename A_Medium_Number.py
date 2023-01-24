test = int(input())

for i in range(test):
    nums = list(map(lambda a: int(a), input().split()))
    nums.sort()
    print(nums[1])
    