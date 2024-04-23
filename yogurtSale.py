# https://codeforces.com/gym/519233/my
import math
def by_regular(n, a ) -> int:
    return a * n

def by_promotion(n, a, b) -> int:
    if n%2 == 0:
        return (math.floor(n / 2) * b)
    else:
        return (math.floor(n / 2) * b) + a


out = []
for _ in range (int(input())):
    x  = input().split()
    out.append(min(by_regular(int(x[0]), int(x[1])),by_promotion(int(x[0]), int(x[1]), int(x[2]))))

for x in out:
    print(x)  
    