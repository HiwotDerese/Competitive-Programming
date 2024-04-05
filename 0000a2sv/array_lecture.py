# array circular traversal

array = [10, 20, 30, 40, 50]
size = len(array)

for index in range(0, 2 * size):
    value = array[index % size]
    print(value)