# -*- coding: utf-8 -*-
from typing import List


def binary_search_recursive(arr: List[int], low: int, high: int, x: int) -> int:
    """
    recursive_version
    如果x in arr，傳回x的index，否則傳回-1
    若x在arr中出現多次時，mid不一定會回傳最先出現的index, 需要再額外的判斷
    """
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            # match
            return mid
        elif arr[mid] > x:
            # take left half
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            # take right half
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        # not match
        return -1


def binary_search_iter(arr: List[int], x: int) -> int:
    """
    iterative_version
    如果x in arr，傳回x的index，否則傳回-1
    若x在arr中出現多次時，mid不一定會回傳最先出現的index, 需要再額外的判斷
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            # take right half
            low = mid + 1
        elif arr[mid] > x:
            # take left half
            upper = mid - 1
        else:
            # match
            return mid
    # not match
    return -1
