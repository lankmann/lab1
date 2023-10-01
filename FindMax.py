import numpy as np
from math import floor


def findMaxLinear(a) -> int:
    '''Takes numpy array and returns the largest element in array'''
    largest = a[0]
    for item in a:
        if item > largest:
            largest = item
    return largest

def findMaxLinearWithCount(a) -> tuple[int, int]:
    '''Takes array `a` and returns tuple (largest number, number of comparisons)'''
    largest = a[0]
    count = 0
    for item in a[1:]:
        if item > largest:
            largest = item
        count += 1
    return (largest, count)

def findMaxDNC(a, i, j) -> int:
    '''Takes numpy array and returns the largest element in array'''
    if i == j:
        return a[i]
    middle = floor((i + j) / 2)
    return max(findMaxDNC(a, i, middle), findMaxDNC(a, middle + 1, j))

def findMaxDNCWithCount(a, i, j) -> tuple[int, int]:
    '''Takes array `a` and returns tuple (largest number, number of comparisons)'''
    if i == j:
        return (a[i], 0)
    middle = floor((i + j) / 2)
    left_largest = findMaxDNCWithCount(a, i, middle)
    right_largest = findMaxDNCWithCount(a, middle + 1, j)
    if left_largest[0] > right_largest[0]:
        return (left_largest[0], left_largest[1] + right_largest[1] + 1)
    return (right_largest[0], left_largest[1] + right_largest[1] + 1)

def findSecondLinear(a):
    largest_element = a[0]
    largest_element_comparisons = []
    for item in a[1:]:
        if item > largest_element:
            largest_element_comparisons.clear()
            largest_element_comparisons.append(largest_element)
            largest_element = item
        else:
            largest_element_comparisons.append(item)
    return findMaxLinear(largest_element_comparisons)

def findSecondLinearWithCount(a):
    largest_element = a[0]
    largest_element_comparisons = []
    comparisons = 0
    for item in a[1:]:
        comparisons += 1
        if item > largest_element:
            largest_element_comparisons.clear()
            largest_element_comparisons.append(largest_element)
            largest_element = item
        else:
            largest_element_comparisons.append(item)
    second_largest, max_comparisons = findMaxLinearWithCount(largest_element_comparisons)
    return second_largest, comparisons + max_comparisons

def findMaxDNCWithComps(a, i, j) -> tuple[int, list[int]]:
    '''Takes array `a` and returns tuple (largest number, list of compared values)'''
    comp_lst = []

    if i == j:
        return (a[i], [])

    middle = floor((i + j) / 2)
    left_max, left_comp = findMaxDNCWithComps(a, i, middle)
    right_max, right_comp = findMaxDNCWithComps(a, middle + 1, j)

    if left_max > right_max:
        comp_lst += left_comp
        comp_lst.append(right_max)
        return (left_max, comp_lst)
    else:
        comp_lst += right_comp
        comp_lst.append(left_max)
        return (right_max, comp_lst)

def findSecondDNC(a):
    right, complst = findMaxDNCWithComps(a, 0, len(a) - 1)
    second_largest = findMaxLinear(complst)
    return second_largest

def findSecondDNCWithCount(a):
    largest, complst = findMaxDNCWithComps(a, 0, len(a) - 1)
    cnt = len(a) - 1
    second_largest, cnt2 = findMaxLinearWithCount(complst)
    total = cnt + cnt2
    return second_largest, total
