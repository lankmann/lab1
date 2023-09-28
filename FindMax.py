import numpy as np;
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