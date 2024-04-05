class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_, n = defaultdict(list), len(nums)

        for i in range(n):
            dic_[nums[i]].append(i)
            diff = target - nums[i]

            if diff in dic_:
                if diff != nums[i]:
                    return [i, dic_[diff][0]]
                
                elif len(dic_[diff]) > 1:
                    for idx in dic_[diff]:
                        if i != idx:
                            return [i, idx]
                
        
