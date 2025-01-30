num_test_cases = int(input())

for _ in range(num_test_cases):
    number = int(input())
    
    answer = 0
    while number > 0:
        answer += number
        number //= 2
    
    print(answer)

# 5, 2, 1  = 9
# 6, 3, 1 = 10