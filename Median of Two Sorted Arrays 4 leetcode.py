"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


def findMedianSortedArrays(nums1, nums2):
    lista = nums1 + nums2
    lista.sort()

    tamanho = len(lista)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        print((lista[meio-1] + lista[meio])/2)
        return (lista[meio-1] + lista[meio])/2
    else:
        print(float(lista[meio]))
        return(float(lista[meio]))


if __name__ == '__main__':
    assert findMedianSortedArrays([1, 3], [2]) == 2.00000
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.50000
    assert findMedianSortedArrays([1, 2, 3], [3, 4, 5]) == 3.00000
    assert findMedianSortedArrays([2, 3], [7, 4, 5]) == 4.00000
