class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        
        if ((len(changed) == 1) or (len(changed)%2 != 0)):
            return original

        else:
            half = len(changed) // 2
            first_half = changed[:half]
            first_half.sort()
            second_half = changed[half:]
            second_half.sort()
            for i in range(half):
                if first_half[i] * 2 == second_half[i]:
                    original.append(first_half[i])
                elif first_half[i] / 2 == second_half[i]:
                    original.append(second_half[i])
                else:
                    break
            if len(original) == half:
                return original
            else:
                return []

            
#         else:
#             changed.sort()
#             for i in range(len(changed) - 1):
#                 for  j in range(i + 1, len(changed),1):
#                     if changed[0] * 2 == changed[j] :
#                         original.append(changed[0])
#                         changed[0].remove()
#                         changed[j].remove()
            
            
        