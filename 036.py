# https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_C

if __name__ == "__main__":
    N, W = map(int, input().split())
    bag = []
    for _ in range(N):
        v, w = list(map(int, input().split()))
        bag.append((v, w))

    dp = [-1 for _ in range(W+1)]
    dp[0] = 0

    for i in range(N):
        iv, iw = bag[i]
        for w in range(iw, W+1):
            if dp[w-iw] == -1:
                continue
            else:
                dp[w] = max(dp[w-iw] + iv, dp[w])

    result = max(dp)

    print(result)
