for _ in range(int(input())):
    num_items, price_a, price_b = map(int, input().split())
    quotient = num_items // 2
    remainder = num_items % 2
    regular_cost = num_items * price_a

    if num_items % 2 == 0:
        promotional_cost = quotient * price_b
    else: 
        promotional_cost = quotient * price_b + remainder * price_a

    print(int(min(regular_cost, promotional_cost)))