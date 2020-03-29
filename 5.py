# https: // atcoder.jp/contests/abc095/tasks/arc096_a


def solve():
    A, B, C, X, Y = map(int, input().split())

    price_no_ab = A * X + B * Y

    if X < Y:
        price_use_ab = A * 0 + B * (Y - X) + C * 2 * X
    else:
        price_use_ab = A * (X - Y) + B * 0 + C * 2 * Y

    if X < Y:
        price_ab = C * 2 * Y
    else:
        price_ab = C * 2 * X

    # print([price_use_ab, price_no_ab, price_ab])
    return min([price_use_ab, price_no_ab, price_ab])


if __name__ == "__main__":
    result = solve()
    print(result)
