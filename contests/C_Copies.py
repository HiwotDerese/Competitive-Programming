import math


n, x, y = list(map(int, input().split()))

ans = min(x, y)

# a, b = 1/x, 1/y
# c = a + b
# x = (n - 1) * (1/c)


# print(math.ceil(x) + ans)
res = math.ceil((n - 1)*x*y /(x + y) + ans)

re= res % min(x, y) 
res += re

print(res)
