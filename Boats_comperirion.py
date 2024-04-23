def count_teams(weights, s):
    count = 0
    used = [False] * len(weights)
    for i in range(len(weights)):
        if not used[i]:
            for j in range(i + 1, len(weights)):
                if not used[j] and weights[i] + weights[j] == s:
                    used[i] = used[j] = True
                    count += 1
                    break
    return count

t = int(input())
a = []
for _ in range(t):
   
    n = int(input())
    weights = list(map(int, input().split()))

    max_weight = sum(weights)

    max_teams = 0
    for s in range(2, max_weight + 1):
        teams = count_teams(weights, s)
        max_teams = max(max_teams, teams)

    a.append(max_teams)
for x in a:
    print(x)
