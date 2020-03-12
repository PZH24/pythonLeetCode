"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
"""
from typing import List


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    len_nums1 = len(nums1)
    if len_nums1 % 2 == 1:
        mid = float(nums1[int((len_nums1 - 1) / 2)])
    else:
        mid = float((nums1[int(len_nums1 / 2)] + nums1[int(len_nums1 / 2 - 1)]) / 2)
    return mid
