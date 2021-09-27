# -*- coding: utf-8 -*-
from typing import List


def prime_table(n: int) -> List[bool]:
    """
    建立整數0~n(包含n)的質數表
    """
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            # Update all multiples of p
            for idx in range(p * p, n + 1, p):
                primes[idx] = False
        p += 1
    return primes
