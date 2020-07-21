# https://www.ioi-jp.org/camp/2010/2010-sp-tasks/2010-sp-day3_22.pdf

# 参考 https://note.nkmk.me/python-union-find/


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True


n, m, k = list(map(int, input().split()))
abcs = [list(map(int, input().split())) for _ in range(m)]
abcs.sort(key=lambda x: x[2])

uf = UnionFind(n)
cost = 0
cnt = 0
for a, b, c in abcs:
    if cnt == n-k:
        break
    a -= 1
    b -= 1
    unioned = uf.union(a, b)
    if unioned:
        cost += c
        cnt += 1

print(cost)
