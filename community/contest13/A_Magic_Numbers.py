r = input()

count = 0

count += r.count("1")
count += r.count("14")
count += r.count("144")

if count == len(r):
    result = "YES"

else:
    result = "NO"

print(result)

# 114114144

# 5, 3, 1 = 6