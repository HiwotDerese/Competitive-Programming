class Solution:
#     [3,2,1,5,6,4]
    def largest(self, nums, n, k, cnt):
            # print(nums)
            pivot = 0
            # if n - k == pivot + cnt:
            #     return nums[pivot]

            read, write = 1, 1

            while read < len(nums):
                if nums[read] <= nums[pivot]:
                    nums[read], nums[write] = nums[write], nums[read]
                    read += 1
                    write += 1

                else:
                    read += 1

            nums[pivot], nums[write - 1] = nums[write - 1], nums[pivot]
            # print(n-k, write - 1)
            # print(nums, cnt, cnt + write - 1 )
            if cnt + write - 1 == n - k:
                return nums[write - 1]

            elif (n - k) < (cnt + write - 1):
                return self.largest(nums[: write - 1], n, k, cnt)
            else:
                
                cnt += write
                return self.largest(nums[write:], n, k, cnt)

    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n, cnt = len(nums), 0
        return self.largest(nums, n, k, cnt)
        
        
        
        