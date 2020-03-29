# https: // atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        Ai = list(map(int, input().split()))
        A.append(Ai)

    result = 0
    for j1 in range(M):
        for j2 in range(j1, M):
            tmp_result = 0
            for i in range(N):
                tmp_result += max(A[i][j1], A[i][j2])
            result = max(result, tmp_result)

    print(result)
