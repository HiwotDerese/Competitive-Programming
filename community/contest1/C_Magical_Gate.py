testCase = int(input())
for _ in range(testCase):

    n, ch = input().split()
    n = int(n)
    s = input().strip()
    
    if ch == 'g':
        print(0)

    else:
        first = -1
        ans = 0
        
        for i in range(n):
            if s[i] == 'g':
                first = i
                break
        
        # ryyggry   3, 
        i = 0
        while i < n:
            if s[i] == ch:
                count = 0
                flag = False
                for j in range(i + 1, n):
                    count += 1
                    if s[j] == 'g':
                        flag = True
                        break
                i += count
                if flag:
                    ans = max(ans, count)
                else:
                    ans = max(ans, count + 1 + first)
            i += 1

        print(ans)
        