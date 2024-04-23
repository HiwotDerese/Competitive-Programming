def cyclicSort(arr):
    index = 0

    while index < len(arr):
        if arr[index] == index + 1:
            index += 1
        else:
            # arr[index], arr[arr[index]- 1]=arr[arr[index] - 1], arr[index] // 1, 4
            # arr[index] = 1
            arr[arr[index] - 1], arr[index] = arr[index], arr[arr[index] - 1] 


    return arr

arry = [4,3,6,5,1,2]
print(cyclicSort(arry))

