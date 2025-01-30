from collections import defaultdict
from bisect import bisect

def maxSubstringLength(self, s: str) -> int:
    n = len(s)
    occurs = defaultdict(list)
    for i, c in enumerate(s):
        occurs[c].append(i)

    def all_letter_in_or_out(l, r, firstC, lastC):
        for c in occurs:
            if not( (c==firstC or c==lastC) or (occurs[c][0] > l and occurs[c][-1] < r) or bisect(occurs[c], l) == bisect(occurs[c], r)):
                return False
        return True

    lengthToBeat = 0
    for firstC, firstVal in occurs.items():
        for lastC, lastVal in occurs.items():
            length = lastVal[-1] - firstVal[0] + 1
            if (length < lengthToBeat) or (length == n):
                continue
            if firstC == lastC and all_letter_in_or_out(firstVal[0], lastVal[-1], firstC, lastC):
                lengthToBeat = length
            if firstVal[-1] > lastVal[-1] or firstVal[0] > lastVal[0]:
                continue
            if all_letter_in_or_out(firstVal[0], lastVal[-1], firstC, lastC):
                lengthToBeat = length
    return lengthToBeat


print(maxSubstringLength("amazonservices"))
