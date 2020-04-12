# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d


def dfs(i, j, t):
    t += 1
    B[i][j] = 0
    tmp_t = t
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ii < 0 or n <= ii:
            continue
        if jj < 0 or m <= jj:
            continue
        if B[ii][jj] == 0:
            continue

        t = max(t, dfs(ii, jj, tmp_t))
    B[i][j] = 1
    return t


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))

    result = 0
    for start_i in range(n):
        for start_j in range(m):
            if A[start_i][start_j] == 0:
                continue
            B = [[A[i][j] for j in range(m)] for i in range(n)]
            d = {}
            d[(start_i, start_j)] = 1
            result = max(result, dfs(start_i, start_j, 0))
    print(result)
