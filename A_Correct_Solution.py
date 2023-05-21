import heapq

n = input()
ans = int(input())

arr = []
correct = []

for i in n:
    arr.append(int(i))

heapq.heapify(arr)

while arr:
    if not correct and arr[0] == 0:
        zeros = []
        
        while arr and arr[0] == 0:
            zeros.append(heapq.heappop(arr))

        if arr:
            correct.append(str(heapq.heappop(arr)))

        while zeros:
            correct.append(str(zeros.pop()))

    else:
        correct.append(str(heapq.heappop(arr)))

num = int(''.join(correct))

if num == ans:
    print('OK')

else:
    print('WRONG_ANSWER')
    