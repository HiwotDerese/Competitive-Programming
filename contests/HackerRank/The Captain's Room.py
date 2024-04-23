# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
roomNum = list(map(lambda a: int(a), input().split(' ')))
dic = {}

for i in roomNum:
    dic[i] = dic.get(i, 0) + 1
    
for i in dic:
    if dic[i] == 1:
        print(i)
        break
        
