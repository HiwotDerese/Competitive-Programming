from collections import defaultdict

q = int(input())

dic = defaultdict(list)
ans = []

for _ in range(q):
    query = list(input().split())
    num1 = int(query[1])

    if query[0] == 'remove' and num1 in ans:
        idx = ans.index(num1)
        ans.pop(idx)

    elif query[0] == 'insert':
        num2 = int(query[2])
        if num2 in ans:
            idx = ans.index(num2)
            ans.insert(idx + 1, num1)

        else:
            ans.append(num1)

    # print(ans, 'loop')

print(*ans)

