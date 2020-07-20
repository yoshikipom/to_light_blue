# https://atcoder.jp/contests/joi2016yo/tasks/joi2016yo_e
# TLE BFSのところで到達済みのチェックがうまくいかない

import collections
import heapq

INF = float('inf')

N, M, K, S = list(map(int, input().split()))
P, Q = list(map(int, input().split()))
d = {i: set() for i in range(N)}
C = [int(input())-1 for _ in range(K)]
X = [list(map(int, input().split())) for _ in range(M)]
for a, b in X:
    a -= 1
    b -= 1
    d[a].add(b)
    d[b].add(a)

COST = [P for _ in range(N)]

for start in C:
    q = collections.deque()
    # (town_id, depth)
    q.append((start, 0))
    while(q):
        item, depth = q.pop()
        if depth > S:
            continue
        COST[item] = Q
        next_list = d[item]
        for next_item in next_list:
            q.appendleft((next_item, depth+1))
for i in C:
    COST[i] = INF
COST[0] = COST[-1] = 0

q = []
result = [INF for _ in range(N)]
result[0] = 0
heapq.heappush(q, (0, 0))
while q:
    cost, item = heapq.heappop(q)
    next_list = d[item]
    if cost == INF:
        continue
    for next_item in next_list:
        next_cost = cost+COST[next_item]
        if next_cost < result[next_item]:
            result[next_item] = next_cost
            heapq.heappush(q, (next_cost, next_item))

print(result[-1])
