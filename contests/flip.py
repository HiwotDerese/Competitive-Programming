def main():
    matrix = [['T', 'T', 'P', 'P', 'P'],]
    k = 3

    mapping = {}
    for row in matrix:
        count = row.count('T')

        if count == k or (k - count >= 0 and (k - count) % 2 != 0):
            key = ''.join(row)
            mapping[key] = mapping.get(key, 0) + 1

    max_value = 0
    for value in mapping.values():
        max_value = max(value, max_value)

    print(max_value)

print(main())