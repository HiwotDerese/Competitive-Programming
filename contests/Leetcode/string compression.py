class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        i = 0
        while(i < len(chars)-1):
            if chars[i] == chars[i+1]:
                count += 1
                chars.pop(i+1)
            else:
                if count > 1:
                    for ch in str(count):
                        chars.insert(i+1, ch)
                        i += 1
                i += 1
                count = 1

        if count > 1:   
            for ch in str(count):     
                chars.insert(i+1, ch)
                i += 1
        
        return len(chars)

