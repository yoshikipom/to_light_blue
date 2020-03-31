# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c

import bisect

if __name__ == "__main__":
    n, m = map(int, input().split())
    P = [0]
    for _ in range(n):
        P.append(int(input()))

    Q = set()
    for i in range(n+1):
        for j in range(n+1):
            Q.add(P[i] + P[j])

    Q = sorted(Q)

    result = 0
    for q in Q:
        if q > m:
            continue
        q_index = bisect.bisect_right(Q, m - q)
        result = max(result, q + Q[q_index-1])

    print(result)
