# -*- coding: utf-8 -*-
from typing import List


def radix_sort(arr: List[int]):
    """
    time complexity為arr中最大數值的位元數
    """
    length = len(arr)
    count = max(arr)  # 資料裡最大的數值

    # 用最大數來判斷最大位數
    digit = 1
    while count > 9:
        count /= 10
        digit += 1

    tmp = []
    cur = 0
    # 資料的大小會決定桶子的數量，會是一個二維陣列
    for i in range(length):
        tmp.append([0] * length)
    # 游標行，用來將資料放到同一位數但不同列的桶子
    order = [0] * length

    if digit <= 9:
        '''use LSD(Least significant digit) method '''
        n = 1
        while n <= max(arr):
            for idx in range(length):
                # 將資料用10來取個位數的餘數
                lsd = int(arr[idx] / n) % 10
                tmp[lsd][order[lsd]] = arr[idx]
                order[lsd] += 1
            for idx in range(length):
                # 如果這個位數的桶子在此行有資料，就丟到同一個位數，但下一列的位置
                if order[idx] != 0:
                    for jdx in range(order[idx]):
                        arr[cur] = tmp[idx][jdx]
                        cur += 1
                # 將游標行的資料歸零
                order[idx] = 0
            n *= 10
            cur = 0
        print(arr)
