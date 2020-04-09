# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d

if __name__ == "__main__":
    D, N = list(map(int, input().split()))
    T = [int(input()) for _ in range(D)]
    A = []
    B = []
    C = []
    for _ in range(N):
        a, b, c = list(map(int, input().split()))
        A.append(a)
        B.append(b)
        C.append(c)

    dp = [[-1 for _ in range(N)] for _ in range(D)]

    for j in range(N):
        t = T[0]
        if A[j] <= t and t <= B[j]:
            dp[0][j] = 0

    for i in range(D-1):
        t = T[i+1]
        for j in range(N):
            if dp[i][j] == -1:
                continue
            c = C[j]

            diff = -1
            next_j = -1
            for jj in range(N):
                if A[jj] <= t and t <= B[jj]:
                    dp[i+1][jj] = max(dp[i+1][jj], dp[i][j] + abs(c-C[jj]))

    # for row in dp:
        # print(*row)
    print(max(dp[D-1]))
