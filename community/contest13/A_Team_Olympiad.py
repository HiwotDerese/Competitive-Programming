# Read the first input (length of the list, but it's not used)
input()

# Initialize a list of three empty lists
a = [[], [], []]

# Read the second input and split it into elements
elements = input().split()

# Populate the lists
for i in range(len(elements)):
    x = int(elements[i])
    a[x-1].append(i + 1)

# Find the minimum length of the sublists
min_length = len(a[0])
for sublist in a[1:]:
    if len(sublist) < min_length:
        min_length = len(sublist)

# Print the minimum length
print(min_length)

# Print the elements in the format as required
for i in range(min_length):
    for sublist in a:
        print(sublist[i], end=' ')
    print()
