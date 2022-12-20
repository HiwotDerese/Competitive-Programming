class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        arrs = 0
        count = 0
        m = k
        i = 0
        for j in range(k):
            arrs += arr[j]
        # for i in range(len(arr)):
        while m < len(arr):
            if arrs / k >= threshold:
                count += 1
            arrs = arrs - arr[i] + arr[m]
            m += 1
            i += 1
        if arrs / k >= threshold:
            count += 1
        return count

#         class Solution:
#   def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#     len_arr = len(arr)
#     res = 0
#     temp = arr[0 : k - 1]
#     curr_sum = sum(temp)
#     for r in range(k - 1, len(arr)):
#       curr_sum += arr[r]
#       print(curr_sum)
#       if curr_sum / k >= threshold:
#         res += 1
#       curr_sum -= arr[r - k + 1]
#     return res
        

