def find_min(r, c, triangle):
    n = len(triangle)

    if r == n:
        return 0

    else:
        minimum = min(
            find_min(r + 1, c, triangle),
            find_min(r + 1, c + 1, triangle)
        )

        return triangle[r][c] + minimum


tri = [
    [2],
    [4, 5],
    [2, 4, 5],
    [4, 5, 6, 7],
    [8, 9, 7, 6, 5]
]

print(find_min(0, 0, tri))