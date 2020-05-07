# https://onlinejudge.u-aizu.ac.jp/problems/DPL_2_A


INF = float('inf')


def rec(bit, v):
    if dp[bit][v] != -1:
        return dp[bit][v]

    if (1 << V) - 1 == bit and v == 0:
        dp[bit][0] = 0
        return 0

    res = INF
    if v in D:
        for to, dist in D[v].items():
            if not (bit & (1 << to)):
                res = min(res, rec(bit | (1 << to), to) + dist)

    dp[bit][v] = res
    return res


if __name__ == "__main__":
    D = {}
    V, E = list(map(int, input().split()))
    for _ in range(E):
        s, t, d = list(map(int, input().split()))
        if s not in D:
            D[s] = {}
        D[s][t] = d

    dp = [[-1] * (V) for _ in range(1 << V)]

    print(dp[0][0] if rec(0, 0) != INF else -1)
