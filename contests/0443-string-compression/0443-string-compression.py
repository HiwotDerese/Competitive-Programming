class Solution:
    def compress(self, chars: List[str]) -> int:
        leng = len(chars)
        chars.append("")
        curr = chars[0]
        count = 0
        
        for i in range(leng+1):
            if chars[0] == curr:
                count += 1
                
            else:
                if count == 1:
                    chars.append(curr)
                else:
                    chars.append(curr)
                    chars += list(str(count))
                curr = chars[0]
                count = 1
                
            chars.pop(0)
                           
        return len(chars)
                
        