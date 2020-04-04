# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_C

from collections import deque


class Data:
    def __init__(self, index, depth):
        super().__init__()
        self.index = index
        self.depth = depth


if __name__ == "__main__":
    n = int(input())
    d = {}
    for _ in range(n):
        u, k, *li = list(map(int, input().split()))
        d[u] = li

    queue = deque()

    result = {}
    for i in range(n):
        result[i+1] = -1

    depth = 0
    queue = deque()
    queue.appendleft(Data(index=1, depth=0))
    while queue:
        data = queue.pop()
        index = data.index
        depth = data.depth
        if result[index] != -1:
            continue
        result[index] = depth

        for child in d[index]:
            queue.appendleft(Data(index=child, depth=depth+1))

    for k, v in result.items():
        print(k, v)
