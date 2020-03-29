# https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c


def calc_square_if_exists(p1, p2, poles_set):
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]
    p3 = (p2[0] + delta_y, p2[1] - delta_x)
    p4 = (p1[0] + delta_y, p1[1] - delta_x)
    p5 = (p2[0] - delta_y, p2[1] + delta_x)
    p6 = (p1[0] - delta_y, p1[1] + delta_x)

    if (p3 in poles_set and p4 in poles_set or
            p5 in poles_set and p6 in poles_set):
        # 正方形があるとき面積
        return delta_x ** 2 + delta_y ** 2
    else:
        # ないときは0
        return 0


def solve():
    N = int(input())
    poles = []

    for _ in range(N):
        x, y = map(int, input().split())
        poles.append((x, y))

    poles_set = set(poles)

    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            if i == j:
                continue
            p1 = poles[i]
            p2 = poles[j]

            square = calc_square_if_exists(p1, p2, poles_set)
            result = max(result, square)

    print(result)


if __name__ == "__main__":
    solve()
