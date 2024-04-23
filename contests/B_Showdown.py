test = int(input())

for t in range(test):
    s = input()
    p1 = 5
    p2 = 5
    score = [0, 0]
    min1, min2 = 10, 10
    for i in range(10):
        if s[i] == '1':
            if i % 2 == 0:
                score[0] += 1
            else:
                score[1] += 1

        elif s[i] == '?':
            if i % 2 == 0:
                score[0] += 1

        if i % 2 == 0:
            p1 -= 1
        else:   
            p2 -= 1

        if score[0] > score[1] + p2 or score[1] > score[0] + p1:
            min1 = i + 1
            break
    
    p1 = 5
    p2 = 5
    score = [0, 0]
    for i in range(10):
        if s[i] == '1':
            if i % 2 == 0:
                score[0] += 1
            else:
                score[1] += 1

        elif s[i] == '?':
            if i % 2 != 0:
                score[1] += 1

        if i % 2 == 0:
            p1 -= 1
        else:   
            p2 -= 1

        if score[0] > score[1] + p2 or score[1] > score[0] + p1:
            min2 = i + 1
            break

    print(min(min1, min2))

    

        


       
