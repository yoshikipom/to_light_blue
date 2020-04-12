# https://onlinejudge.u-aizu.ac.jp/problems/1166

from collections import deque


class Point:
    def __init__(self):
        super().__init__()
        self.up = 1
        self.down = 1
        self.left = 1
        self.right = 1


def solve(W, H):
    Points = {}
    for i in range(H):
        for j in range(W):
            point = Point()
            Points[(i, j)] = point

    for i in range(H * 2 - 1):
        if i % 2 == 0:
            # | | | vertical
            walls = list(map(int, input().split()))
            for j, wall in enumerate(walls):
                Points[(i//2, j)].right = wall
                Points[(i//2, j + 1)].left = wall
        else:
            # - - - horizontal
            walls = list(map(int, input().split()))
            for j, wall in enumerate(walls):
                Points[(i//2, j)].down = wall
                Points[(i//2 + 1, j)].up = wall

    queue = deque()
    queue.appendleft((0, 0, 1))
    checked = set()
    goal = (H-1, W-1)

    result = 0
    while queue:
        # print(queue)
        i, j, d = queue.pop()
        if (i, j) in checked:
            continue
        checked.add((i, j))

        if (i, j) == goal:
            result = d
            break

        point = Points[(i, j)]
        tmp_d = d+1
        if point.up == 0:
            queue.appendleft((i-1, j, tmp_d))
        if point.down == 0:
            queue.appendleft((i+1, j, tmp_d))
        if point.left == 0:
            queue.appendleft((i, j-1, tmp_d))
        if point.right == 0:
            queue.appendleft((i, j+1, tmp_d))

    print(result)


if __name__ == "__main__":
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break

        solve(W, H)
