test = int(input())
# i = input().split()
# print(i)

for i in range(test):
    tshirt_size = input().split()
    t_size1 = tshirt_size[0]
    t_size2 = tshirt_size[1]
    leng1 = len(t_size1)
    leng2 = len(t_size2)

    # l < m < s
    if t_size1[-1] < t_size2[-1]:
        print(">")
    elif t_size1[-1] > t_size2[-1]:
        print("<")

    # when both are the same ll,mm or ss
    else:
        if leng1 == leng2:
            print("=")
        elif t_size1[-1] == "S":
            if leng1 < leng2:   
                print(">")
            elif leng1 > leng2:
                print("<")
        elif t_size1[-1] == "L":
            if leng1 < leng2:   
                print("<")
            elif leng1 > leng2:
                print(">")

  
    
    
    
    
