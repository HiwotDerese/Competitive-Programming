
import collections
def minWindow(s, t):
        dic1, dic2 = collections.Counter(t), collections.Counter()

        left, _min, ans = 0, float('inf'), ""
        
        for right in range(len(s)):
            while dic1 <= dic2:
                
                if right - left < _min:
                    ans = s[left:right]
                    _min = right - left

                dic2[s[left]] -= 1
                left += 1

            dic2[s[right]] += 1
            
            right += 1
            
        return ans

print(minWindow("ADOBECODEBANC", "ABC"))





