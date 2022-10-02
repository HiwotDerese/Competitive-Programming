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
        

