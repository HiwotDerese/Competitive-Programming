# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
engSub = set(input().split())

m = int(input())
frenchSub = set(input().split())

ans = len(engSub.union(frenchSub))
print(ans)
