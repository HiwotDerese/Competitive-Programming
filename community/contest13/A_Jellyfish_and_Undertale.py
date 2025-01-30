num_test_cases = int(input())

for _ in range(num_test_cases):
    a, b, n = map(int, input().split())
    
    numbers = [int(x) for x in input().split()]
    
    for i in numbers:
        b += min(a-1, i)
    
    print(b)