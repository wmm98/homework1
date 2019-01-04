'''给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。'''


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.  # 不需要返回，修改列表内容即可
    """
    # if len(nums) >= k:
    #     length = len(nums)
    #     num1 = [0 for i in range(length)]
    #     for i in range(length):
    #         if i + k < length:
    #             num1[i + k] = nums[i]
    #         else:
    #             num1[k - (length - 1 - i) - 1] = nums[i]
    #     return num1

    # 方法一：
    # length = len(nums)
    # i = k % length
    # nums[:] = nums[-i:] + nums[:-i]


    lens = len(nums)
    for i in range(k):
        x = nums[-1]
        nums.pop(-1)
        nums.insert(0, x)
    return nums

num = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
result = rotate(num, k1)
print(result)
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]