class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            maxVal = max(arr[:len(arr)-i]) 
            maxIdx = arr.index(maxVal)+1
            arr[:maxIdx] = reversed(arr[:maxIdx])
            ans.append(maxIdx)
            arr[:len(arr)-i] = reversed(arr[:len(arr)-i])
            ans.append(len(arr)-i)
        return ans


        