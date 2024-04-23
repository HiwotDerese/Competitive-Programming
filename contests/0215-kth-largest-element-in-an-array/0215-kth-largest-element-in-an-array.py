class Solution:
    def largest(self, nums, n, k, cnt):
            pivot = 0
            read, write = 1, 1

            while read < len(nums):
                if nums[read] <= nums[pivot]:
                    nums[read], nums[write] = nums[write], nums[read]
                    read += 1
                    write += 1

                else:
                    read += 1

            nums[pivot], nums[write - 1] = nums[write - 1], nums[pivot]

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
        
        
        
        