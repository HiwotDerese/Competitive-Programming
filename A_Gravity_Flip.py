n = int(input())

cubes = list(map(int, input().split()))
ans = sorted(cubes)
print(" ".join(map(str, ans)))
   