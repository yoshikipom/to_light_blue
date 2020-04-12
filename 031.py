# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e

from collections import deque

if __name__ == "__main__":
    W, H = map(int, input().split())
    A = []
    A.append([-1] * (W + 4))
    A.append([-1, 0] + [0] * W + [0, -1])
    for _ in range(H):
        row = list(map(int, input().split()))
        A.append([-1, 0] + row + [0, -1])
    A.append([-1, 0] + [0] * W + [0, -1])
    A.append([-1] * (W + 4))

    # for row in A:
    # print(*row)

    queue = deque()
    queue.appendleft((1, 1))

    cnt = 0
    while queue:

        # print(queue)
        i, j = queue.pop()
        if A[i][j] == -1:
            continue
        A[i][j] = -1
        if i % 2 == 1:
            d_list = [(-1, -1), (-1, 0), (0, -1),
                      (0, 1), (1, -1), (1, 0)]
        else:
            d_list = [(-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, 0), (1, 1)]

        for di, dj in d_list:
            ii = i + di
            jj = j + dj
            if A[ii][jj] == -1:
                continue
            elif A[ii][jj] == 0:
                queue.appendleft((ii, jj))
            elif A[ii][jj] == 1:
                # print('debug: i {} j {} ii {} jj {}'.format(i, j, ii, jj))
                cnt += 1

    print(cnt)
