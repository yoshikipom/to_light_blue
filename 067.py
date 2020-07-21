# https://atcoder.jp/contests/abc065/tasks/arc076_b
import copy


class UnionFind():
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True


n = int(input())
rows = [[i] + list(map(int, input().split())) for i in range(n)]

# (start, end, cost)
edges = []

# x座標でソートしてx座標が隣り合う点にをedge候補に
rows_x = copy.deepcopy(rows)
rows_x.sort(key=lambda x: x[1])
for i in range(len(rows)-1):
    left = rows_x[i]
    right = rows_x[i+1]
    edges.append((left[0], right[0], right[1] - left[1]))

# print(rows)
rows_y = copy.deepcopy(rows)
rows_y.sort(key=lambda x: x[2])
for i in range(len(rows)-1):
    down = rows_y[i]
    up = rows_y[i+1]
    edges.append((down[0], up[0], up[2] - down[2]))

# print(edges)

uf = UnionFind(n)

edges.sort(key=lambda edge: edge[2])

result = 0
for edge in edges:
    s, t, c = edge
    unioned = uf.union(s, t)
    if unioned:
        result += c

print(result)
