# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e

from collections import deque


class Point:
    def __init__(self, i, j, d):
        super().__init__()
        self.i = i
        self.j = j
        self.d = d

    def __repr__(self):
        return 'i {} j {} d {}'.format(self.i, self.j, self.d)


def calc_d(start_i, start_j, goal_i, goal_j):
    B = [[A[i][j] for j in range(W+2)] for i in range(H+2)]
    queue = deque()
    queue.appendleft(Point(start_i, start_j, 0))
    while queue:
        point = queue.pop()
        if point.i == goal_i and point.j == goal_j:
            return point.d

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i = point.i + di
            j = point.j + dj
            if B[i][j] != 'X':
                B[i][j] = 'X'
                queue.appendleft(Point(i, j, point.d+1))


if __name__ == "__main__":
    H, W, N = map(int, input().split())
    A = []
    A.append(['X' for _ in range(W+2)])
    for _ in range(H):
        row = ['X'] + [c for c in input()] + ['X']
        A.append(row)
    A.append(['X' for _ in range(W+2)])

    d = {}
    for i in range(H+2):
        for j in range(W+2):
            if A[i][j] == 'S':
                start_i = i
                start_j = j
            elif A[i][j] not in ['.', 'X']:
                d[int(A[i][j])] = (i, j)

    result = 0

    now_i = start_i
    now_j = start_j
    for i in range(1, N+1):
        goal_i, goal_j = d[i]
        result += calc_d(now_i, now_j, goal_i, goal_j)
        now_i = goal_i
        now_j = goal_j

    print(result)
