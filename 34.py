# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_A

if __name__ == "__main__":
    n = int(input())

    if n == 0 or n == 1:
        result = 1
    else:
        A = [1] * (n + 1)

        for i in range(2, n+1):
            A[i] = A[i-1] + A[i-2]

        result = A[n]

    print(result)
