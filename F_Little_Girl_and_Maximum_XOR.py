l, r = list(map(int, input().split()))

k = l ^ r

k = (k).bit_length()

print((2 ** k) - 1)

