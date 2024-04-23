from operator import index


n = int(input())

cubes = list(map(int, input().split()))

print(" ".join(map(str,cubes.sort())))
   