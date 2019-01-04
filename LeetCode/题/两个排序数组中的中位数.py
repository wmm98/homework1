'''给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:

s1 = [1, 3]
s2 = [2]

中位数是 2.0
示例 2:
s1 = [1, 2]
s2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5'''


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    '''当样本数为奇数时，中位数=(N+1)/2 ; 当样本数为偶数时，中位数为N/2与1+N/2的均值 '''

    if len(nums1) > 0 and len(nums2) > 0:
        nums = nums1 + nums2
        nums3 = sorted(nums)
        if len(nums3) % 2 == 0:
            center1 = nums3[len(nums3) // 2 - 1]
            center2 = nums3[len(nums3) // 2]
            center_result = (center1 + center2) / 2
        else:
            center_result = float(nums3[len(nums3) // 2])
        return center_result
    elif len(nums1) == 0 and len(nums2) == 0:
        return 0
    else:
        if len(nums1) != 0:
            if len(nums1) % 2 == 0:
                center1 = nums1[len(nums1) // 2 - 1]
                center2 = nums1[len(nums1) // 2]
                center_result = (center1 + center2) / 2
                return center_result
            else:
                return float(nums1[len(nums1) // 2])
        else:
            if len(nums2) % 2 == 0:
                center1 = nums2[len(nums2) // 2 - 1]
                center2 = nums2[len(nums2) // 2]
                center_result = (center1 + center2) / 2
                return center_result
            else:
                return float(nums2[len(nums2) // 2])



s1 = []
s2 = []
# s1 = [1, 3]
# s2 = [2]
do_result = findMedianSortedArrays(s1, s2)
print(do_result)
