n = int(input())
times = list(map(int, input().split()))

alice_bars = 0
bob_bars = 0
left = 0
right = n - 1

alice_time = 0
bob_time = 0

while left <= right:
    if alice_time <= bob_time:
        alice_time += times[left]
        alice_bars += 1
        left += 1
    else:
        bob_time += times[right]
        bob_bars += 1
        right -= 1

print(alice_bars, bob_bars)