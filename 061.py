# https://atcoder.jp/contests/abc012/tasks/abc012_4
N, M = list(map(int, input().split()))

INF = float('inf')
G = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, t = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a][b] = t
    G[b][a] = t

for i in range(N):
    G[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

# for row in G:
#     print(' '.join(map(str, row)))

print(min(map(max, G)))
