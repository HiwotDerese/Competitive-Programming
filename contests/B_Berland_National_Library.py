n = int(input())

dic, inside, max_ = {}, 0, 0
for _ in range(n):
    v = input().split()

    if v[0] == "+":
        inside += 1
        dic[v[1]] = 1
        max_ = max(max_, inside)

    elif v[0] == "-":
        if v[1] in dic and dic[v[1]] != 0:
            inside -= 1

        else:
            max_ += 1

print(max_)

        

