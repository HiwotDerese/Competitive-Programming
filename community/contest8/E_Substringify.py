n = int(input())

st = []
for _ in range(n):
    st.append(input())

st.sort(key=len)

for i in range(n - 1):
    if st[i] not in st[i + 1]:
        print("NO")
        exit()

print("YES")
for s in st:
    print(s)