test = int(input())
for i in range(test):

    n, m, k = list(map(int, input().split()))

    s1 = sorted(input().strip(), reverse=True)

    s2 = sorted(input().strip(), reverse=True)

    ans = ""
    count1 = 0
    count2 = 0

    while len(s1) > 0 and len(s2) > 0:
        
        if s1[-1] < s2[-1]:
            if count1 == k:
                ans += s2.pop()
                count2 += 1
                count1 = 0
            else:
                ans += s1.pop()
                count1 += 1
                count2 = 0
        else:
            if count2 == k:
                ans += s1.pop()
                count1 += 1
                count2 = 0
            else:
                ans += s2.pop()
                count2 += 1
                count1 = 0

    print(ans)




        






# test_cases = int(input().strip())
# for _ in range(test_cases):
#     n, m, k = map(int, input().strip().split())
#     first_arr = input().strip()
#     second_arr = input().strip()
#     first_arr = sorted(first_arr, reverse=True)
#     second_arr = sorted(second_arr, reverse=True)
#     a_count, b_count = 0, 0
#     result = []
#     while len(first_arr) > 0 and len(second_arr) > 0:
#         choose_second = second_arr[-1] < first_arr[-1]
#         if choose_second and b_count == k:
#             choose_second = False
#         if not choose_second and a_count == k:
#             choose_second = True
 
#         if choose_second:
#             result.append(second_arr.pop())
#             b_count += 1
#             a_count = 0
#         else:
#             result.append(first_arr.pop())
#             a_count += 1
#             b_count = 0
 
#     result = "".join(result)
#     print(result)





