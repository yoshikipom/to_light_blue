# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/13
import itertools


def check(Queens, L):
    # row
    for i in range(L):
        cnt = 0
        for j in range(L):
            if (i, j) in Queens:
                cnt += 1
        if cnt != 1:
            return False

    # colmn
    for j in range(L):
        cnt = 0
        for i in range(L):
            if (i, j) in Queens:
                cnt += 1
        if cnt != 1:
            return False

    # diagonally
    for i in range(L):
        cnt = 0
        for i in range(L):
            if (i, j) in Queens:
                cnt += 1
        if cnt != 1:
            return False

    for queen in Queens:
        i = queen[0] - 1
        j = queen[1] - 1
        while 0 <= i and 0 <= j:
            if (i, j) in Queens:
                return False
            i -= 1
            j -= 1
        i = queen[0] - 1
        j = queen[1] + 1
        while 0 <= i and j < 8:
            if (i, j) in Queens:
                return False
            i -= 1
            j += 1
        i = queen[0] + 1
        j = queen[1] - 1
        while i < 8 and 0 <= j:
            if (i, j) in Queens:
                return False
            i += 1
            j -= 1
        i = queen[0] + 1
        j = queen[1] + 1
        while i < 8 and j < 8:
            if (i, j) in Queens:
                return False
            i += 1
            j += 1

    return True


def print_result(Queens, L):
    for i in range(L):
        for j in range(L):
            if (i, j) in Queens:
                print('Q', end='')
            else:
                print('.', end='')
        print()


if __name__ == "__main__":

    num_of_queen = 8
    L = 8
    k = int(input())

    GivenQueens = set()
    for i in range(k):
        r, c = map(int, input().split())
        GivenQueens.add((r, c))

    A = [i for i in range(L)]
    for pernutated in itertools.permutations(A, L-k):
        Queens = set(GivenQueens)
        row = 0
        i = 0
        while len(Queens) < num_of_queen:
            if row not in list(map(lambda queen: queen[0], Queens)):
                Queens.add((row, pernutated[i]))
                i += 1
            row += 1

        if check(Queens, L):
            print_result(Queens, L)
            break
