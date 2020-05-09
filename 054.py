# https://atcoder.jp/contests/abc006/tasks/abc006_4
import bisect

N = int(input())

C = []
for _ in range(N):
    c = int(input())
    C.append(c)

INF = float('inf')
dp = [INF for _ in range(N)]

for i in range(N):
    c = C[i]
    target_index = bisect.bisect_left(dp, c)
    dp[target_index] = c

no_move_card_cnt = bisect.bisect_left(dp, INF)
print(N - no_move_card_cnt)
