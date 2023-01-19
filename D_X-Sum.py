  
from collections import defaultdict
test = int(input())

for i in range(1):

    nm = list(map(lambda a: int(a), input().split()))
    row = nm[0]
    col = nm[1]

    # accept the matrix
    matrix = []
    for i in range(row):
        arr = list(map(lambda a: int(a), input().split()))
        matrix.append(arr)
    print(matrix)
    sum_right = matrix
    sum_left = matrix
    # print(sum_right)
    # print(sum_left)
    for i in range(1,row):
        for j in range(col):
            # if i == 0:
            #     continue
            if j == 0:
                # sum_right[i][j] = matrix[i][j]
                sum_left[i][j] += sum_left[i - 1][j + 1]
            elif j == col - 1:
                # sum_left[i][j] = matrix[i][j]
                sum_right[i][j] = matrix[i][j] + sum_left[i - 1][j - 1]
            else:
                sum_left[i][j] = matrix[i][j] + sum_left[i - 1][j + 1]
                sum_right[i][j] = matrix[i][j] + sum_left[i - 1][j - 1]

    print(sum_right)
    print(sum_left)


    # diff = collections.defaultdict(int)
    # add = collections.defaultdict(int)

    # for row in range(rows):
    #     for col in range(cols):
            
    #         diff[row - col] += matrix[row][col]
    #         add[ row + col] += matrix[row][col]

    # maximal_res = 0

    # for row in range(rows):
    #     for col in range(cols):
    #         maximal_res= max(maximal_res, diff[row - col] + add[ row + col]- matrix[row][col])

    # print(maximal_res)




