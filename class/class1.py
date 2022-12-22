l = [1,2,3,4,5]
# for i in range(len(l)):
#     print(l[~i])

a = [[]] * 5
a[0].append(5)
# print(a)
a2 = [[] for i in range(5)]
a2[0].append(5)
# print(a2)

# tuples no add or delete but concatenate
t1 = (1,2) + (3,4)
# print(t1)
# no compresion
setA = set([1,2,3,4])
setB = set((1.7,9,9))
setc = set("a")
setc = set("a", "b", "c")
print(setA)
print(setB)
print(setc)