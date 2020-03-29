# https: // atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b


def calc_dist(start, a, b, end):
    return abs(a - start) + abs(b - a) + abs(end - b)


def solve():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    start = sorted(A)[N//2]
    end = sorted(B)[N//2]

    result = sum([calc_dist(start, A[i], B[i], end) for i in range(N)])

    print(result)


if __name__ == "__main__":
    solve()
