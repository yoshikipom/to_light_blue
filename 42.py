# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    D = []
    for _ in range(N):
        D.append(int(input()))
    C = []
    for _ in range(M):
        C.append(int(input()))

    dp = [[0] + [float('inf') for _ in range(N)] for _ in range(M+1)]

    # 各日
    for j in range(M):
        # 各都市
        for i in range(N):
            if dp[j][i] == float('inf'):
                continue
            dp[j+1][i+1] = min(dp[j][i+1], dp[j][i] + D[i] * C[j])

    print(dp[-1][-1])
