class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_arr, max_arr, n, min_, max_ = [inf], [-inf], len(nums), inf, -inf
        
        for idx in range(n):
            min_ = min(min_, nums[idx])
            max_ = max(max_, nums[-(idx + 1)])
            min_arr.append(min_)
            max_arr.append(max_)

        max_arr.sort(reverse = True)

        for idx in range(n):
            if min_arr[idx] < nums[idx] < max_arr[idx]:
                return True