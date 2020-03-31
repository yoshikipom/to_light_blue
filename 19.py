# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b


def binary_search(D, k, n):
    l = 0
    r = n
    while l <= r:
        c = (l + r) // 2
        if k < D[c]:
            r = c - 1
        elif k == D[c]:
            return 0
        elif D[c] < k:
            l = c + 1

    return min(abs(k-D[r]), abs(k-D[l]))


if __name__ == "__main__":
    d = int(input())
    n = int(input())
    m = int(input())
    D = [int(input()) for _ in range(n - 1)]
    K = [int(input()) for _ in range(m)]
    D = [0] + sorted(D) + [d]

    result = 0
    for k in K:
        result += binary_search(D, k, n)

    print(result)
