import collections
n, k = list(map(int, input().split()))

if k > (n).bit_count():
    print("NO")

else:
    arr, power, flag = collections.deque([]), 0,0
    while n:
        if n % 2 != 0:
            arr.append(2 ** power)

        power += 1
        n >> 1


    while arr[-1] != 1:
        num = arr.pop()
        if num // 2 == 1:
            arr.appendleft(num // 2)
            arr.appendleft(num // 2)

        else:
            arr.append(num // 2)
            arr.append(num // 2)

        if len(arr) == k:
            print("YES")
            print(arr)
            flag = 1
            break

    if not flag:
        print("NO")


    


