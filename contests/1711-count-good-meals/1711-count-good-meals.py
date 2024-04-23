class Solution:
    
    def countPairs(self, deliciousness: List[int]) -> int:

        dict_del = Counter(deliciousness)
        ans = 0
        
        for x in dict_del:
            if x == 0: 
                continue
#            if the number it self is power of 2
            if ceil(log2(x)) == floor(log2(x)):
                
                combination = dict_del[x]*(dict_del[x] - 1) // 2
                ans += combination
                
#           if the number is power of 2 with another number
            m = 2**ceil(log2(x)) - x
            if m in dict_del:
                ans += dict_del[x] * dict_del[m]

        return ans % 1000000007
    