class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = sorted(heights, reverse=True)
        ans = []
        for i in range(len(arr)):
            indx = heights.index(arr[i])
            ans.append(names[indx])
        return ans
