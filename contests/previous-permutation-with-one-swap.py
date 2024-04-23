class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n =  len(arr)
        min_ = (arr[-1], -1)

        for idx in range(-2, -(n + 1), -1):
            if arr[idx] > min_[0]:

                max_, num = (-inf, 0), arr[idx]
                for i in range(idx + 1, 0, 1):
                    if arr[i] < num and arr[i] > max_[0]:
                        max_ = (arr[i], i)  
                        
                swap_idx = max_[1]
                arr[n + swap_idx], arr[n + idx]  = arr[n + idx], arr[n + swap_idx]
                return arr

            elif arr[idx] < min_[0]:
                min_ = (arr[idx], idx)

        return arr