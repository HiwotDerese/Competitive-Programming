def brute(list, k):
    leng = len(list)
    _max = 0

    for i in range(leng-k + 1):
        _sum = 0

        for j in range(i,i+k):
            _sum += list[j]

        _max = max(_max, _sum)

    return _max

print(brute([0,1,2,3,4,5], 3))



def sliding(list, k):
    leng = len(list)
    _sum = 0
    _max = 0

    i = j = 0
    
    while j < leng:
        if j - i + 1 <= k:
            _sum += list[j]
            j += 1 
        else:
            _max = max(_max, _sum)
            _sum -= list[i]
            _sum += list[j]

            












