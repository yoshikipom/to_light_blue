# https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a
import itertools
n, m = map(int, input().split())
B = [0] + [int(input()) for _ in range(n-1)]
A = [int(input()) for _ in range(m)]

X = list(itertools.accumulate(B))
# print(X)

cur = 0
result = 0
for a in A:
    result += abs(X[cur + a] - X[cur])
    result %= 10**5
    cur += a

print(result)
