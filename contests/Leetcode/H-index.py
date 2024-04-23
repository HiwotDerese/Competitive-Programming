class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        low = 0
        high = n - 1
        while low <= high:
            middle = low + (high - low)/2
            if n - int(middle) == citations[int(middle)]:
                return citations[int(middle)]
            elif n - int(middle) > citations[int(middle)]:
                low = int(middle) + 1
            else:
                high = int(middle) -1
        return n - low
        
                