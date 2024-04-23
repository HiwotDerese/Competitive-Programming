n = int(input())
arr = list(map(lambda a: int(a), input().split()))
s_array = sorted(arr)

if s_array == arr:
    print("yes")
    print("1 1")
else:
    l = 0
    r = n-1
    # [0,1,2,3,4]
    while l < n:
        if arr[l] != s_array[l]:
            break
        else:
            l += 1
    while r > -1:
        if arr[r] != s_array[r]:
            break
        else:
            r -= 1
    sliced = arr[l:r+1]
    rev = sorted(sliced, reverse=True)
    if sliced == rev:
        print("yes")
        print(str(l+1) + " " + str(r+1))
    else:
        print("no")


    


    # idx = []
    # for i in range(n):
    #     if arr[i] != s_array[i]:
    #         idx.append(i)
    # if len(idx) > 2:
    #     print("no")
    # else:
    #     left = idx[0]
    #     right = idx[1]
    #     sliced = arr[left:right+1]
    #     rev = sorted(sliced, reverse=True)

    #     arry = sliced
    #     if arry == rev:
    #         print("yes")
    #         print(str(left+1) + " " + str(right+1))
    #     else:
    #         print("no")




