# https://atcoder.jp/contests/abc122/tasks/abc122_b


def is_acgt(c):
    acgt = ['A', 'C', 'G', 'T']

    return c in acgt


if __name__ == "__main__":
    S = input()

    result = 0
    tmp_result = 0
    for c in S:
        if (is_acgt(c)):
            tmp_result += 1
            result = max(result, tmp_result)
        else:
            tmp_result = 0

    print(result)
