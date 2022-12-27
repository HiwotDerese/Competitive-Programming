# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
fal = 0

for i in range(n):
    set1 = set(input().split())
    if set1.issubset(A) and len(A) > len(set1):
        continue
    else:
        print(False)
        fal += 1
        break
if fal == 0:
    print(True)
