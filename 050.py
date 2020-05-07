# https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_g

INF = float('inf')

# input
N, M = map(int, input().split())
MAP = [[(INF, -1) for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s, t, d, time = map(int, input().split())
    MAP[s - 1][t - 1] = MAP[t - 1][s - 1] = (d, time)

# solve by DP
# dp[staus(bit)][last distnation][0: cost, 1:count] bitは1のところが到達前
dp = [[[INF, 1] for _ in range(N)] for _ in range(1 << N)]
dp[(1 << N) - 1][0] = [0, 1]

for status in range((1 << N) - 1, -1, -1):

    # 出発点と到着点を全組み合わせ試す
    for dist in range(N):
        for prev in range(N):

            # prevが到達前のときは無視
            if (status >> prev) & 1:
                continue

            # 閉鎖済みの道のときは無視
            if dp[status | 1 << prev][prev][0] + MAP[dist][prev][0] > MAP[dist][prev][1]:
                continue

            prev_status = status | 1 << prev
            next_cost = dp[prev_status][prev][0] + MAP[dist][prev][0]
            next_cost_count = dp[prev_status][prev][1]
            if dp[status][dist][0] > next_cost:
                dp[status][dist][0] = next_cost
                dp[status][dist][1] = next_cost_count
            elif dp[status][dist][0] == next_cost:
                dp[status][dist][1] += next_cost_count

# output
if dp[0][0][0] < INF:
    print(*dp[0][0])
else:
    print("IMPOSSIBLE")
