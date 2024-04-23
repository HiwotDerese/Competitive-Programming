n = int(input())
matrix = []
source = []
sink = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    if sum(matrix[i]) == 0:
        sink.append(i + 1)

    col = 0
    for j in range(n):
        col += matrix[j][i]

    if col == 0:
        source.append(i + 1)
  
print(len(source), *source)
print(len(sink), *sink)

