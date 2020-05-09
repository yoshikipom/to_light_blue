# https://atcoder.jp/contests/abc134/tasks/abc134_e

import bisect

N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

A.reverse()
INF = float('inf')
dp = [INF for _ in range(N)]

for a in A:
    target_index = bisect.bisect_right(dp, a)
    # print(a, target_index)
    dp[target_index] = a

# print(dp)
print(bisect.bisect_left(dp, INF))
