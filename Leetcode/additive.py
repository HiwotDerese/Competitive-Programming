
# def additive2(num, num1, num2, sum_, index):
#     if index == len(num) - 1:
#         # print(num, num1, num2, sum_, index)
#         if num1 + num2 == sum_:
#             return True
#         else:
#             return False
    
#     if num1 + num2 == sum_:
        
#         return additive2(num, int(num2), int(sum_), int(num[index]), index)  
    
#     elif num1 + num2 > sum_:
#         # num2 = int(str(num2) + num[index])
#         idx = index + 1
#         num2 = int(str(num2) + num[index])
#         for i in range(index + 1, len(num)):
#             return additive2(num, num1, num2, int(num[idx : i+1]), i) 
        
#     else:
#         return
    


# def additive1(num, num1, num2, sum_, index):
#     if index == len(num) - 1:
#         # print(num, num1, num2, sum_, index)
#         if num1 + num2 == sum_:
#             return True
#         else:
#             return False
    
#     if num1 + num2 == sum_:
        
#         return additive1(num, int(num2), int(sum_), int(num[index]), index)  
        
#     elif num1 + num2 > sum_:
#         # num2 = int(str(num2) + num[index])
#         idx = index + 1
#         num2 = int(str(num2) + num[index])
#         for i in range(index + 1, len(num)):
#             return additive2(num, num1, num2, int(num[idx : i+1]), i) 
        
#     else:
#         return 
def additive1(num, num1, num2, sum_, index):
    
def isAdditiveNumber(num):
    if len(num) < 3:
        return False
    else:
        for i in range(len(num)):
            if 1 + len(num[i + 1:]) < 3:
                return False
            index = i + 2
            additive1(num, int(num[:i+1]), int(num[i+1:i+2]), int(num[i+2:i+3]), index)
            if additive1:
                return True
            
        return False
    
print(isAdditiveNumber("199100"))
# "112358"




