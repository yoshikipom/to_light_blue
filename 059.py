# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e
# 1つだけMLE

from collections import deque
import heapq


N, K = list(map(int, input().split()))
C = []
R = []
# iから直接乗っていける点
d1 = {i: set() for i in range(N)}
# iからのタクシーでたどり着ける点
d2 = {i: set() for i in range(N)}
for _ in range(N):
    c, r = list(map(int, input().split()))
    C.append(c)
    R.append(r)
for _ in range(K):
    a, b = list(map(int, input().split()))
    d1[a-1].add(b-1)
    d1[b-1].add(a-1)


for target in range(N):
    q = deque()
    q.appendleft((target, 0))
    while q:
        index, depth = q.pop()
        if index in d2[target]:
            continue

        if index != target:
            d2[target].add(index)

        if depth + 1 > R[target]:
            continue

        for next_index in d1[index]:
            q.appendleft((next_index, depth+1))

del d1
del R


INF = 10000 * N
Costs = [INF for _ in range(N)]
Costs[0] = 0
q = []
heapq.heappush(q, (0, 0))
while q:
    cost, index = heapq.heappop(q)
    next_cost = cost + C[index]
    for next_index in d2[index]:
        if next_cost < Costs[next_index]:
            Costs[next_index] = next_cost
            heapq.heappush(q, (next_cost, next_index))

print(Costs[-1])
