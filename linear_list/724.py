def pivotIndex(nums):
	total_sum = sum(nums)
	left_sum = 0
	for i in range(len(nums)):
		if left_sum == total_sum - left_sum - nums[i]:
			return i
		left_sum += nums[i]
	return -1

def pivotIndex2(nums):
	total_sum = sum(nums)
	left_sum = 0
	for i, num in enumerate(nums):
		if left_sum == total_sum - left_sum - num:
			return i
		left_sum += nums[i]
	return -1

nums = [1, 7, 3, 6, 5, 6]
print(pivotIndex(nums))
print(pivotIndex2(nums))

nums = [1, 2, 3]
print(pivotIndex(nums))
print(pivotIndex2(nums))