# -*- coding: utf-8 -*-
from typing import List


def bubble_sort(arr: List[int]):
    n = len(arr)
    for idx in range(n - 2):
        for jdx in range(n - idx - 1):
            if arr[jdx] > arr[jdx + 1]:
                # swap
                arr[jdx], arr[jdx + 1] = arr[jdx + 1], arr[jdx]
