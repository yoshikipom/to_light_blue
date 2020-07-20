# https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A
import heapq

N, M, r = list(map(int, input().split()))

D = {}
for i in range(N):
    D[i] = []

for _ in range(M):
    s, t, d = list(map(int, input().split()))
    D[s].append((t, d))

A = []
heapq.heappush(A, (0, r))

INF = float('inf')
results = [INF for _ in range(N)]
results[r] = 0

while A:
    cost, a = heapq.heappop(A)
    for t, d in D[a]:
        next_cost = cost + d
        if next_cost < results[t]:
            results[t] = next_cost
            heapq.heappush(A, (next_cost, t))

for result in results:
    if result == INF:
        print('INF')
    else:
        print(result)
