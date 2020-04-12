# https://onlinejudge.u-aizu.ac.jp/problems/1611
# TLE


def solve(N, A):
    ans = -1
    dp = [[0] * (N+1) for _ in range(N+1)]

    for w in range(2, N+1):
        for l in range(N):
            r = l + w
            if r > N:
                continue
            # print('l {}, r {} w {}'.format(l, r, w))
            if dp[l+1][r-1] == w - 2 and abs(A[l] - A[r-1]) <= 1:
                dp[l][r] = w

            for mid in range(l, r+1):
                # print('l {}, r {} mid {}'.format(l, r, mid))
                next_tmp = max(dp[l][r], dp[l][mid] + dp[mid][r])
                ans = max(ans, next_tmp)
                dp[l][r] = next_tmp

    print(ans)


if __name__ == "__main__":
    while True:
        N = int(input())

        if N == 0:
            break

        A = list(map(int, input().split()))

        solve(N, A)
