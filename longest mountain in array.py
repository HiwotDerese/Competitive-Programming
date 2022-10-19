class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3 or len(list(set(arr))) == 1:
            return 0
        start = 0 
        maxm = 0
        reachedPeak = False
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                reachedPeak = True
            elif arr[i-1] >= arr[i] <= arr[i+1]:
                if reachedPeak:
                    reachedPeak = False
                    maxm = max(maxm, i - start + 1)
                start = i
            
        if reachedPeak:
            maxm = max(maxm, len(arr) - start)
        return maxm
        