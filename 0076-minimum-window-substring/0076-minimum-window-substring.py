class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t) # counter for t to check with
        window = Counter() # sliding window
        ans = "" # answer
        last = 0 # last index in our window
        
        for i,char in enumerate(s):
            
            window[char] = window.get(char,0)+1 # add this character to our window
            
            while window >= tCounter: # while we have all the necessary characters in our window
                if ans == "" or i - last < len(ans): # if the answer is better than our last one
                    ans = s[last:i+1] # update ans
                    
                window[s[last]] -= 1 # remove the last element from our counter
                last += 1 # move the last index forward
                
        return ans # return answer
#     def minWindow(self, s: str, t: str) -> str:
#         tCounter = Counter(t) 
#         window = Counter() 
#         ans = "" 
#         last = 0 

#         for i,char in enumerate(s):
#             window[char] = window.get(char,0)

#             while window >= tCounter: 
#                 if ans == "" or i - last < len(ans):
#                     ans = s[last:i+1] 

#                 window[s[last]] -= 1
#                 last += 1

#         return ans 
    #         dic1, dic2 = Counter(t), Counter()

#         left, _min, ans = 0, float('inf'), ""
        
#         for right in range(len(s)):
#             while dic1 <= dic2:
#                 if right - left < _min:
#                     ans = s[left:right]
#                     _min = right - left

#                 dic2[s[left]] -= 1
#                 left += 1

#             dic2[s[right]] = 1
            
#             right += 1
            
#         return ans
                
                
        
        
        
        
        
        