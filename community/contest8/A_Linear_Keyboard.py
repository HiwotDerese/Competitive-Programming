test = int(input())

for _ in range(test):
    s = input()
    s2 = input()
    order = {}

    for i, char in enumerate(s):
        if char not in order:
            order[char] = i
    # print(order)
    n, ans = len(s2), 0

    for i in range(n-1):
        
        ans += abs(order[s2[i]] - order[s2[i+1]])

    print(ans)