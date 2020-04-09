# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d


def count_change_color(colmn, color):
    cnt = 0
    for row in range(5):
        if A[row][colmn] == color:
            cnt += 1
    return 5 - cnt


if __name__ == "__main__":
    N = int(input())

    INF = N * 5

    A = []
    for _ in range(5):
        row = input()
        A.append([c for c in row])

    color_list = ['B', 'R', 'W']
    dp = [[INF for _ in range(3)] for _ in range(N)]

    for j, color in enumerate(color_list):
        dp[0][j] = count_change_color(0, color)

    for i in range(1, N):
        for j, color1 in enumerate(color_list):
            for k, color2 in enumerate(color_list):
                if color1 == color2:
                    continue
                dp[i][k] = min(dp[i][k],
                               dp[i-1][j] + count_change_color(i, color2))

    # print(dp)
    print(min(dp[-1]))
