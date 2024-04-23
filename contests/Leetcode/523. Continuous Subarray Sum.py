class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        arr = [nums[0]]
        for i in range(1,len(nums),1):
            arr.append(arr[i - 1] + nums[i])
        arr.insert(0,0)
        print(arr)
        hashT = {}
        for i in range(len(arr)):
            rem = arr[i] % k
            if rem in hashT:
                if i - hashT[rem] >= 2:
                    return True
                # else:
                #     hashT[rem] = i
            else:
                hashT[rem] = i
        return False

        # i, j = 0, 1
        # while j < len(nums):
        #     sums = arr[j]
        #     while i < j:
        #         if sums % k == 0:
        #             return True
        #         sums = arr[j] - arr[i]
        #         i += 1
        #     j += 1
        #     i = 0
        # return False

            