class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        hashT = Counter(arr)
        ans, i, n = 0, 0, len(arr)
        while i < n:
            left, right = i, n-1 
            while left < right: 
                if arr[i] + arr[left] + arr[right] < target:
                    left += hashT[arr[left]]
                elif arr[i] + arr[left] + arr[right] > target:
                    right -= hashT[arr[right]]
                else:
                    if arr[i] != arr[left] != arr[right]:
                        ans += hashT[arr[i]] * hashT[arr[left]] * hashT[arr[right]]
                    elif arr[i] == arr[left] != arr[right]:
                        ans += hashT[arr[i]] * (hashT[arr[i]]-1) * hashT[arr[right]]//2 
                    elif arr[i] != arr[left] == arr[right]:
                        ans += hashT[arr[i]] * hashT[arr[left]] * (hashT[arr[left]]-1)//2
                    else:
                        ans += hashT[arr[i]] * (hashT[arr[i]]-1) * (hashT[arr[i]]-2)//6
                    left += hashT[arr[left]]
                    right -= hashT[arr[right]]
            i += hashT[arr[i]]
        return ans % (10 ** 9 + 7)