# Enter your code here. Read input from STDIN. Print output to STDOUT
num = input().split()
n = int(num[0])
m = int(num[1])

group_A = []
group_B = []

ans1 = ""
ans2 = ""

for i in range(n):
    group_A.append(input())
for i in range(m):
    group_B.append(input())

for i in range(m):
    if group_B[i] in group_A:
        for j in range(n):
            if group_A[j] == group_B[i]:
                ans1 += str(j + 1) + " "
        print(ans1)
        ans1 = ""
    else:
        print(-1)
                
             