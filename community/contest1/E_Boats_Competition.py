test = int(input())

for _ in range(test):
    n = int(input())
    arr = map(int, input().split())

    weight_freq = {}
    for weight in arr:
        weight_freq[weight] = weight_freq.get(weight, 0) + 1

    max_teams = 0
    for s in range(2, 2 * n + 1):
        teams = 0
        for weight in weight_freq:
            complement = s - weight
            if complement in weight_freq:
                teams += min(weight_freq[weight], weight_freq[complement])

        teams //= 2
        max_teams = max(max_teams, teams)

    print(max_teams)