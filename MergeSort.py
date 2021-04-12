import time

import numpy as np


def Merge(data, Draw, left, right, middle):
    Draw(data, ['black' for x in range(len(data))])
    time.sleep(0.35)

    left_temp = data[left:middle + 1]
    right_temp = data[middle + 1: right + 1]

    l = r = 0

    for i in range(left, right + 1):
        if l < len(left_temp) and r < len(right_temp):
            if left_temp[l] <= right_temp[r]:
                data[i] = left_temp[l]
                l += 1
            else:
                data[i] = right_temp[r]
                r += 1

        elif l < len(left_temp):
            data[i] = left_temp[l]
            l += 1
        else:
            data[i] = right_temp[r]
            r += 1

    Draw(data, ['red' if x >= left and x <= right  else 'black' for x in range(len(data))])
    time.sleep(0.35)
    Draw(data, ['green' for x in range(len(data))])


def Merge_Sort_1(data, Draw, left, right):
    if left < right:
        middle = (left + right) // 2
        Merge_Sort_1(data, Draw, left, middle)
        Merge_Sort_1(data, Draw, middle + 1, right)
        Merge(data, Draw, left, right, middle)


def Merge_Sort(data, Draw):
    Merge_Sort_1(data, Draw, 0, len(data) - 1)
