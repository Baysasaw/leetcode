def main():
    n, m = map(int, input().split())
    sizes = [list(map(int, input().split())) for _ in range(n)]
    sizes.sort(key=lambda x: x[0] - x[1], reverse=True)


    compress_size = sum(s[1] for s in sizes)
    initial_size = sum(s[0] for s in sizes)
    a_b = [s[0]-s[1] for s in sizes]

    if compress_size > m:
        return -1
    elif initial_size == m:
        return 0
    else:
        count = 0
        for size in sizes:
            initial_size -= size[0] - size[1]
            count += 1
            if initial_size <= m:
                break
        return count'=