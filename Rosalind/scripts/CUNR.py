def CUNR(n):
    from operator import mul
    return reduce(mul,range(1,2*n-5+1,2)) % 10**6


def ROOT(n):
    return CUNR(n) * (2 * n - 3) % 10 ** 6

print ROOT(812)

