# -*- coding: utf-8 -*-
from typing import List


def quick_sort(arr: List[int], left: int, right: int):
    if left >= right:
        return

    idx = left
    jdx = right
    pivot = arr[left]

    while idx != jdx:
        while arr[jdx] > pivot and idx < jdx:
            # 從右邊開始找，找比基準點小的值
            jdx -= 1
        while arr[idx] <= pivot and idx < jdx:
            # 從左邊開始找，找比基準點大的值
            idx += 1
        if idx < jdx:
            # 當左右索引值沒有相遇時，互換值
            arr[idx], arr[jdx] = arr[jdx], arr[idx]

            # 將基準點歸換至代理人相遇點
    arr[left] = arr[idx]
    arr[idx] = pivot

    # 繼續處理較小部分的子循環
    quick_sort(arr, left, idx - 1)
    # 繼續處理較大部分的子循環
    quick_sort(arr, idx + 1, right)
