class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashm = {}
        for i in range(len(nums)):
            if nums[i] in hashm:
                if abs(hashm[nums[i]] - i) <= k:
                    return True
                else:
                    hashm[nums[i]] = i
            else:
                hashm[nums[i]] = i
        return False
                