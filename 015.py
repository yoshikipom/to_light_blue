# https://atcoder.jp/contests/abc145/tasks/abc145_c

import itertools


def calc_dist(p1, p2):
    x_delta = p1[0] - p2[0]
    y_delta = p1[1] - p2[1]
    return (x_delta ** 2 + y_delta ** 2) ** (1/2)


if __name__ == "__main__":
    N = int(input())
    A = []
    for _ in range(N):
        x, y = map(int, input().split())
        A.append((x, y))

    dist_list = []
    for permutated in itertools.permutations(A):
        dist = 0
        for i in range(1, len(permutated)):
            dist += calc_dist(permutated[i], permutated[i-1])
        dist_list.append(dist)

    print(sum(dist_list) / len(dist_list))
