test = int(input())

for i in range(test):
    input1 = list(map(lambda a: int(a), input().split()))
    orbits = list(map(lambda a: int(a), input().split()))
    count = 0

    dic = {}
    for i in range(input1[0]):
        dic[orbits[i]] = dic.get(orbits[i], 0) + 1
    
    for i in dic:
        if dic[i] >= input1[1]:
            count += input1[1]
        else:
            count += dic[i]
    print(count)



