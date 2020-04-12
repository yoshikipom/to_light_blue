# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d

if __name__ == "__main__":
    N, K = map(int, input().split())
    plans = {}
    for _ in range(K):
        day, source = list(map(int, input().split()))
        plans[day] = source

    dp = [[[0]*3 for _ in range(3)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(3):
            for k in range(3):
                ls = [plans[i+1] - 1] if i + 1 in plans else [0, 1, 2]
                for l in ls:
                    if i >= 2 and j == k == l:
                        continue
                    dp[i+1][k][l] += dp[i][j][k]

    # for row in dp:
    #     print(*dp)

    print(sum(sum(dp[-1], [])) % 10 ** 4)
