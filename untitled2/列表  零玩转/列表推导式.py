nums = [1, 2, 3, 4, 5]

# 生成一个元素的平方的列表
nums1 = [num ** 2 for num in nums]
print(nums1)  # [1, 4, 9, 16, 25]

nums3 = [num ** 2 for num in nums if num % 2 == 0]
print(nums3)  # [4, 16]


nums2 = [num + 1 for num in nums]
print(nums2)  # [2, 3, 4, 5, 6]