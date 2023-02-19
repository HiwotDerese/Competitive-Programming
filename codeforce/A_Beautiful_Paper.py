test = int(input())


for i in range(test):
    first = list(map(lambda a: int(a), input().split()))
    second = list(map(lambda a: int(a), input().split()))

    sums = 0
    j = 0
    first.sort(reverse = True)

    for i in range(2):
        if first[i] in second:
                val = first[i]
                first.remove(val)
                second.remove(val)
                sums = first[0] + second[0]

                if sums == val:
                    print("Yes")
                    j += 1
                else:
                    print("No")
                    j += 1
                break          
        else:
            continue

    if j == 0:
        print("No")




        
            
