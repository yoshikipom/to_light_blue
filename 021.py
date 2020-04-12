# https://atcoder.jp/contests/abc023/tasks/abc023_d


def check(H, S, x, n):
    Deadlines = []
    for i in range(n):
        deadline = (x-H[i])/S[i]
        Deadlines.append(deadline)

    Deadlines.sort()

    for i in range(n):
        if (Deadlines[i] < i):
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    H = []
    S = []
    for _ in range(n):
        h, s = map(int, input().split())
        H.append(h)
        S.append(s)

    # for i in range(1, 30):
        # print(i)
        # print(check(H, S, i, n))

    l = 0
    r = max(H) + n * max(S)
    while l < r:
        c = (l + r) // 2
        if check(H, S, c, n):
            r = c
        else:
            l = c + 1

    print(r)
