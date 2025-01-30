from typing import Counter
test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    dic = Counter(arr)
    print(max(dic.values()))