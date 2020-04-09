# https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_B


if __name__ == "__main__":
    N, W = list(map(int, input().split()))
    bag = []
    for _ in range(N):
        v, w = list(map(int, input().split()))
        bag.append((v, w))

    d = {}

    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    for i in range(N):
        for w in range(W+1):
            iv, iw = bag[i]
            if w >= iw:
                dp[i+1][w] = max(dp[i][w-iw] + iv, dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]

    print(max(dp[N]))
