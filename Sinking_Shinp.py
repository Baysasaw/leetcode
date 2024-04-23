
def evacuation_order(crew):
    priority = {'rat': 1, 'woman': 2, 'child': 2, 'man': 3, 'captain': 4}
    return priority[crew[1]]


n = int(input())
crew = [input().split() for _ in range(n)]


sorted_crew = sorted(crew, key=evacuation_order)


for member in sorted_crew:
    print(member[0])
