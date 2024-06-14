n = int(input())
array = input().strip()

if n <= 50:
    R = B = G = 0

    for i in range(n - 1):
        if array[i] == 'R' and array[i + 1] == 'R':
            R += 1
        elif array[i] == 'B' and array[i + 1] == 'B':
            B += 1
        elif array[i] == 'G' and array[i + 1] == 'G':
            G += 1

    sum_ = R + G + B
    print(sum_)