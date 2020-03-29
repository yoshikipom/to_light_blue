# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_A


def number_list(A):
    number_list = set()
    for bit in range(1 << len(A)):
        sum_a = 0
        for i in range(len(A)):
            if bit & (1 << i):
                sum_a += A[i]
                number_list.add(sum_a)
    return number_list


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    M = list(map(int, input().split()))

    number_list = number_list(A)

    for m in M:
        if m in number_list:
            print('yes')
        else:
            print('no')
