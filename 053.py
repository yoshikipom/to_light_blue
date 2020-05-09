# https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_D
import bisect

INF = float('inf')

n = int(input())
A = []
for _ in range(n):
    a = int(input())
    A.append(a)

dp = [INF for _ in range(n)]

for a in A:
    update_index = bisect.bisect_left(dp, a)
    dp[update_index] = a

print(bisect.bisect_left(dp, INF))
