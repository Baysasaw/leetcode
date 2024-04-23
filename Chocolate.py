
n = int(input())
bars = list(map(int, input().split()))

alice_bars = bob_bars = 0
alice_time = bob_time = 0
left = 0
right = n - 1

while left <= right:
    # Alice's turn
    if alice_time <= bob_time:
        alice_time += bars[left]
        alice_bars += 1
        left += 1
    
    else:
        bob_time += bars[right]
        bob_bars += 1
        right -= 1

print(alice_bars, bob_bars)
