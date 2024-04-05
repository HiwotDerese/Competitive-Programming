from math import factorial, log2


tc = int(input())
for _ in range(tc):
    n = int(input())
    nums = list(map(int, input().split()))
    maxBit = log2(max(nums))
    maxBit = int(maxBit) + 1
    tracked = set()
    prefix = []
    answer = 0
    for i in range(maxBit, -1, -1):
        for num in nums:
            if num & (1 << i) and num not in tracked:
                prefix.append(num)
        m = len(prefix)
        if m > 1:
            answer += factorial(m) // (factorial(2) * factorial(m - 2))
        tracked |= set(prefix)
        prefix.clear()
    print(answer)
        
        

