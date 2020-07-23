# https://atcoder.jp/contests/abc084/tasks/abc084_d
from itertools import accumulate


def get_prime(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        return []
    if n == 2:
        return [2]
    prime = [2]
    limit = int(n ** 0.5)
    nums = [i + 1 for i in range(2, n, 2)]
    while True:
        p = nums[0]
        if limit < p:
            return prime + nums
        prime.append(p)
        nums = [e for e in nums if e % p != 0]


primes = set(get_prime(10 ** 5))
like = [0] * 10 ** 5
for i in range(3, 10**5):
    if i in primes and (i + 1) // 2 in primes:
        like[i] = 1

like_accum = list(accumulate(like))

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    result = like_accum[r] - like_accum[l-1]
    print(result)
