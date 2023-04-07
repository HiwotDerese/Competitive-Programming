test = int(input())

for i in range(test):

    leng = int(input())
    arr = list(map(int, input().split()))

    bit_arr = []

    for i in range(leng):
        num = int((bin(arr[i])[2:]))
        bit_arr.append(len(str(num)))
    
    ans = 0
    for i in range():
        
