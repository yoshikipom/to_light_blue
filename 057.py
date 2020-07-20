# https://atcoder.jp/contests/abc134/tasks/abc134_e
import heapq

n, k = list(map(int, input().split()))


def calc(a, b, A):
    queue = []
    heapq.heappush(queue, (0, a))
    costs = [INF for _ in range(n)]
    costs[a] = 0

    while queue:
        cost, item = heapq.heappop(queue)
        for to, to_cost in enumerate(A[item]):
            if to_cost == INF:
                continue
            next_cost = cost + to_cost
            if next_cost < costs[to]:
                costs[to] = next_cost
                heapq.heappush(queue, (next_cost, to))

    return costs[b]


INF = float('inf')
A = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(k):
    operation, *other = list(map(int, input().split()))

    if operation == 1:
        # 道を追加
        c, d, e = other
        c -= 1
        d -= 1
        A[c][d] = min(A[c][d], e)
        A[d][c] = min(A[d][c], e)

    elif operation == 0:
        # 経路案内
        a, b = other
        a -= 1
        b -= 1
        result = calc(a, b, A)
        if result == INF:
            print(-1)
        else:
            print(result)

    else:
        raise Exception('error', operation)
