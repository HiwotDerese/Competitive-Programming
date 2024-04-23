class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1

        prev = 1
        for idx in range(n):
            if abs(prev - arr[idx]) > 1:
                prev += 1
                arr[idx] = prev

            else:
                prev = arr[idx]

        return arr[-1]