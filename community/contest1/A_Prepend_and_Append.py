test = int(input())

for i in range(test):
    n = int(input())
    bit = input()

    if n < 2:
        print(n)

    else:
        left, right = 0, n - 1
        f = True
        while left <= right:
            if bit[left] == bit[right]:
                print(right - left + 1)
                f = False
                break
            left += 1
            right -= 1         

        if f:
            print(0)