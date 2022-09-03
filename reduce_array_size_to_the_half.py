class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = []
        s = Counter(arr)
        for i in s:
            freq.append(s[i])
        freq.sort()
        freq = list(reversed(freq))
        count = 0
        summ = 0
        for i in freq:
            count += 1
            summ += i
            if len(arr) - summ <= len(arr) / 2:
                return count
   
    
        