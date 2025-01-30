n = int(input())

encrypted = input()
s = ''
index = 0
count = 1


while index < n:
    s += encrypted[index]
    index += count
    count += 1

print(s)