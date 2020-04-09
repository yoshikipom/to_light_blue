# https://onlinejudge.u-aizu.ac.jp/problems/2199
# TLE


def solve():
    dp = [[1000000 for j in range(256)] for _ in range(N+1)]
    dp[0][128] = 0

    for i in range(N):
        for j in range(0, 256):
            for code in code_book:
                next_j = j + code
                if next_j < 0:
                    next_j = 0
                if 255 < next_j:
                    next_j = 255
                dp[i+1][next_j] = min(dp[i+1][next_j],
                                      dp[i][j] + (X[i] - next_j)**2)

    print(min(dp[-1]))


if __name__ == "__main__":
    while(True):
        N, M = list(map(int, input().split()))

        if N == 0 and M == 0:
            break

        code_book = set()
        for _ in range(M):
            code_book.add(int(input()))

        X = []
        for _ in range(N):
            x = int(input())
            X.append(x)

        solve()
