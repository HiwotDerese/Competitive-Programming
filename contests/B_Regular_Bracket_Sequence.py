brackets = input()
ans = 0
stack = []
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
    else:
        if len(stack) > 0:
            stack.pop()
        else:
            ans += 1

ans += len(stack)
print(len(brackets) - ans)