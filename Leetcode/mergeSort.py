

# # def mergeSort(left, right, arr):
# #     if left == right:
# #         return [arr[left]]
 
# #     mid = left + (right - left) // 2
# #     left_half = mergeSort(left, mid, arr)
# #     right_half = mergeSort(mid + 1, right, arr)

# #     return merge(left_half, right_half)
 

# # def merge(left_half, right_half):
# #     i = 0
# #     j = 0
# #     sorted_arr = []
# #     while i < len(left_half) and j < len(right_half):
# #         if left_half[i] < right_half[j]:
# #             sorted_arr.append(left_half[i])
# #             i += 1
# #         else:
# #             sorted_arr.append(right_half[j])
# #             j += 1

    
# #     if i < len(left_half):
# #         while i < len(left_half):
# #             sorted_arr.append(left_half[i])
# #             i += 1

# #     if j < len(right_half):
# #         while j < len(right_half):
# #             sorted_arr.append(right_half[j])
# #             j += 1

# #     # sorted_arr.extend(left_half[i:])
# #     # sorted_arr.extend(right_half[j:])

# #     return sorted_arr

# # def test():
# #  assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10],"Not Implemented Properly"
# #  assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not ImplementedProperly"
# #  assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not ImplementedProperly"
# #  print("Great Job !!!")


# # test()






# # ******************************************************** quick sort

# def quickSort(arr):
#     if len(arr) <= 1:
#         return 
    
#     pivot, read, write = 0, 1, 1
#     while read < len(arr):
#         if arr[read] < arr[pivot]:
#             arr[read], arr[write] = arr[write], arr[read]
#             read += 1
#             write += 1

#         else:
#             read += 1
#     arr[pivot], arr[write - 1] = arr[write - 1], arr[pivot]
#     quickSort(arr[:write])
#     quickSort(arr[write:]) 

#     #  arr, write, end
# #  arr, start, write - 2
# arr = [2,1,4,8,6,5,9]
# # 2 1 4 8 6 5 9
# print(quickSort(arr))




# # def quickSort(arr, start, end):
#     # if end - start <= 0:
#     #     return 
    
#     # pivot = arr[start]
#     # write = start + 1
#     # for read in range(start + 1, end + 1):
#     #     if arr[read] <= pivot:
#     #         arr[read], arr[write] = arr[write], arr[read]
# print(bin(-9))
# print(4 & 1 | 2)
# print(2 | 1 & 4)
# print(3 & 4 | 2)
# print(2 | 4 & 3)

