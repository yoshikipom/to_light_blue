# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque


class Point:
    def __init__(self, x, y, d):
        super().__init__()
        self.x = x
        self.y = y
        self.d = d

    def __repr__(self):
        return 'x {} y {} d {}'.format(self.x, self.y, self.d)


if __name__ == "__main__":
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sy -= 1
    sx -= 1
    gx -= 1
    gy -= 1
    A = []
    for _ in range(R):
        row = [c for c in input()]
        A.append(row)

    queue = deque()
    queue.appendleft(Point(sx, sy, 0))

    result = -1
    while queue:
        point = queue.pop()
        if point.x == gx and point.y == gy:
            result = point.d
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = point.x + dx
            y = point.y + dy
            if A[y][x] == '.':
                A[y][x] = '#'
                queue.appendleft(Point(x, y, point.d+1))

    print(result)
