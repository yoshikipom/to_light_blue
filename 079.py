# https://atcoder.jp/contests/abc106/tasks/abc106_d
n, m, q = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(m)]
Q = [list(map(int, input().split())) for _ in range(q)]

A = [[0 for _ in range(n+1)] for _ in range(n+1)]
for x in X:
    l, r = x
    A[l][r] += 1

B = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        B[i][j] += B[i][j-1] + A[i][j]
    for j in range(1, n+1):
        B[i][j] += B[i-1][j]

for q in Q:
    a, b = q
    result = B[b][b] - B[b][a-1] - B[a-1][b] + B[a-1][a-1]
    print(result)
