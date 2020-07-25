# https://atcoder.jp/contests/abc149/tasks/abc149_f
# TLE
import sys
sys.setrecursionlimit(10**8)
mod = 10**9 + 7

N = int(input())
G = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = set()
parent = [-1 for i in range(N+1)]
count = [1 for i in range(N+1)]
ans = N*pow(2, N-1, mod)


def dfs(node):
    visited.add(node)
    for child in G[node]:
        if child not in visited:
            parent[child] = node
            dfs(child)
    for child in G[node]:
        if child != parent[node]:
            count[node] += count[child]


start = -1
for i in range(1, N+1):
    if len(G[i]) == 1:
        start = i
        break
dfs(start)

ans = 0
for i in range(1, N+1):
    if len(G[i]) > 1:
        ans += pow(2, N-1, mod)
        for x in G[i]:
            if x != parent[i]:
                ans -= pow(2, count[x], mod)
        ans -= pow(2, N-count[i], mod)
        ans += len(G[i]) - 1
        ans %= mod
D = pow(2, N, mod)
print(ans*pow(D, mod-2, mod) % mod)
