# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    vertical = []
    n = int(input())
    block = list(map(lambda a: int(a), input().split(' ')))
    left = 0
    right = n - 1
    while right >= left:
        if not vertical:
            if block[left] >= block[right]:
                vertical.append(block[left])
                left += 1
            else:
                vertical.append(block[right])
                right -= 1
        else:
            if block[left] >= block[right] and vertical[-1] >= block[left]:
                vertical.append(block[left])
                left += 1
            elif block[right] >= block[left] and vertical[-1] >= block[right]:
                vertical.append(block[right])
                right -= 1
            else:
                break
    if len(vertical) == n:
        print("Yes")
    else:
        print("No")
                
        
        
            