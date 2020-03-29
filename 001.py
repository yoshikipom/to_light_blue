# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_B


def solve(n, x):

    result = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            for k in range(j, n+1):
                # 重複はダメ
                if i == j or j == k or k == i:
                    continue

                if i + j + k == x:
                    result += 1

    return result


if __name__ == "__main__":
    while True:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            break

        print(solve(n, x))
