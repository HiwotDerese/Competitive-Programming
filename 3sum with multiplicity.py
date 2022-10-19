class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        unique = list(set(arr))
        unique.sort()
        hashT = Counter(arr)
        i, ans = 0, 0
        while i < len(unique):
            left, right = i, len(unique) - 1
            target2 = target - unique[i]
            while left <= right:
                if unique[left] + unique[right] > target2:
                    right -= 1
                elif unique[left] + unique[right] < target2:
                    left += 1
                else:
                    if unique[i] != unique[left] != unique[right]:
                        ans += hashT[unique[i]] * hashT[unique[left]] * hashT[unique[right]]
                    elif unique[i] == unique[left] != unique[right]:
                        ans += hashT[unique[i]] * (hashT[unique[i]] - 1) * hashT[unique[right]] // 2
                    elif unique[i] != unique[left] == unique[right]:
                        ans += hashT[unique[i]] * hashT[unique[left]] * (hashT[unique[right]] - 1) // 2
                    else:
                        ans += hashT[unique[i]] * (hashT[unique[i]]-1) * (hashT[unique[i]]-2)//6
                        
                    left += 1
                    right -= 1
            i += 1
        return ans % (10 ** 9 + 7)