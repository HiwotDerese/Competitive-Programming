test = int(input())

for _ in range(test):
    n = int(input())
    first, second, both = [], [], []
    for _ in range(n):
        arr = list(input().split())
        if arr[1][0] == "1" and arr[1][1] == "1":
            both.append(int(arr[0]))
        elif arr[1][0] == "1":
            first.append(int(arr[0]))
        elif arr[1][1] == "1":
            second.append(int(arr[0]))

    both.sort()
    first.sort()
    second.sort()
    # print(both, first, second, "hereee")

    if both and first and second:
        
        if first[0] + second[0] <= both[0]:
            print(first[0] + second[0])
        else:
            print(both[0])

    elif both:
        print(both[0])

    elif first and second:
        print(first[0] + second[0])

    else:
        print(-1)



