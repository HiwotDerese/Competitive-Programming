class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorArr = [arr[0]]
        ans = []
        for i in range(1,len(arr)):
            xorArr.append(xorArr[i - 1] ^ arr[i])
        # print(xorArr)
        for i in range(len(queries)):
            # start = queries[i][0]
            # end = queries[i][1]
            if queries[i][0] == 0:
                ans.append(xorArr[queries[i][1]])
            else:
                
                # print(start)
                ans.append(xorArr[queries[i][1]] ^ xorArr[queries[i][0] - 1])
        return ans
