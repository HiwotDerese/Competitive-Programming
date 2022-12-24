inputs = int(input())
ans = ""

for i in range(inputs):
    info = input()
    leng = len(info)
    
    for i in range(leng):
        
        if info[i] == "#":
            ans += " "
            continue
        else:
            ans += info[i]
            
    print(ans)
    ans = ""
