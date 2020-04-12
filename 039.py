# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    counts = [0 for i in range(21)]
    counts[A[0]] = 1

    for i in range(1, N - 1):
        # print('i {} Ai {}'.format(i, A[i]))
        next_counts = [0 for i in range(21)]
        for j in range(21):
            # print('{} {}'.format(i, j))
            # print(next_counts)
            if 0 <= j + A[i] and j + A[i] <= 20:
                next_counts[j + A[i]] += counts[j]
            if 0 <= j - A[i] and j - A[i] <= 20:
                next_counts[j - A[i]] += counts[j]
        # print(next_counts)
        counts = next_counts

    print(counts[A[-1]])
