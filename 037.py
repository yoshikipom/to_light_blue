# https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_A

INF = float('inf')

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    dp = [INF for _ in range(N+1)]
    dp[0] = 0

    for i in range(M):
        c = C[i]
        for n in range(c, N+1):
            if dp[n-c] == INF:
                continue
            else:
                dp[n] = min(dp[n-c] + 1, dp[n])

    print(dp[N])
