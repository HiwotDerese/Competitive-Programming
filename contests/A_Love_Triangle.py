n = int(input())

arr, flag = list(map(int, input().split())), 0

for i in range(len(arr)):
    index2 = arr[i] - 1
    index3 = arr[index2] - 1
    if i == arr[index3] - 1 and i != index2 - 1:
        print("YES")
        flag = 1
        break


if flag == 0:
    print("NO")

