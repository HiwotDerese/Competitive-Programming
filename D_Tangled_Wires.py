s = input()

st = []

for i in s:
    if st and st[-1] == i:
        st.pop()
    else:
        st.append(i)

if len(st) == 0:
    print("Yes")
else:
    print("No")