n, m, k = list(map(int, input().split()))
emotes = list(map(int, input().split()))

count, sum_, leng = 0, 0, len(emotes)
emotes.sort()

if emotes[leng-1] == emotes[leng - 2]:
    print(emotes[leng-1] * m)
else:

    i = 0
    while count < m and i < k:
        sum_ += emotes[leng - 1]
        count += 1
        i += 1

    if count < m:
        sum_ += emotes[leng - 2]
        count += 1

    a = m / count
    _sums = a * sum_
    q = m - (a * count)
    _sums += (q * emotes[leng - 1])

    print(int(_sums))
