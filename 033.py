# https://atcoder.jp/contests/abc088/tasks/abc088_d

from collections import deque

if __name__ == "__main__":
    H, W = list(map(int, input().split()))
    A = []
    A.append('#' * (W + 2))
    for i in range(H):
        A.append('#' + input() + '#')
    A.append('#' * (W + 2))

    # for row in A:
    #     print(row)

    queue = deque()
    queue.appendleft((1, 1, 1))
    checked = set()
    goal = (H, W)

    dist = -1
    while queue:
        i, j, d = queue.pop()
        if (i, j) in checked:
            continue
        checked.add((i, j))

        if (i, j) == goal:
            dist = d

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ii = i + dx
            jj = j + dy
            if A[ii][jj] == '.':
                queue.appendleft((ii, jj, d+1))

    if dist == -1:
        result = -1
    else:
        white = sum([row.count('.') for row in A])
        result = white - dist
    print(result)
