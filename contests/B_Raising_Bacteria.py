x = int(input())
ans = 1

def double(num):
    if num == 1:
        return ans
    
    else:
        if num % 2 == 0:
            return double(num // 2)
        
        else:
            return double((num - 1) // 2) + 1
        

print(double(x))

# print(1 & (1 << 2))



