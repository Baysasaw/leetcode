def can_reach_volume(holes, blocked, A, B):
    total_blocked = sum(holes[i] for i in blocked)
    total_unblocked = sum(holes) - total_blocked
    return (holes[0] * A) / (total_blocked + total_unblocked) >= B

def find_min_holes_to_block(holes, A, B):
    left, right = 0, len(holes) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        blocked = set(range(mid, len(holes)))
        
        if can_reach_volume(holes, blocked, A, B):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

# Input
n, A, B = map(int, input().split())
holes = list(map(int, input().split()))

# Output
print(find_min_holes_to_block(holes, A, B))
