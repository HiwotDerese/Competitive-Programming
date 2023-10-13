q = int(input())
map_ = {}
for _ in range(q):
    a, b = input().split()
    if a in map_:
        map_[b] = map_.pop(a)
    else:
        map_[b] = a

    # print(map_)

print(len(map_))
for a, b in map_.items():
    print(b, a)















# n = int(input())
# map_ = {}
# for _ in range(n):
#     pair = input().split()
#     # print(pair[0])
#     map_[pair[0]] = pair[1]

# # print(map_)

# def findNew(name, dic_):
#     # print(name, "funcc")
#     if name not in dic_.keys():
#         return name
    
#     return findNew(dic_[name], dic_)

# ans = []
# for old in map_:
#     if old not in map_.values():
#         new = findNew(old, map_)
#         # print(new)
#         ans.append((old, new))
#         # print(ans, "ansss")

#         # print(old, new)

# print(len(ans))
# for idx in range(len(ans)):
#     print(ans[idx][0], ans[idx][1])





