def binary_search(a, key, l, r):
	#"""二分查找，找到key应该插入的位置（降序）"""
	while (l < r):
		mid = (l + r + 1) // 2
		if (a[mid][0] >= key):
			l = mid
		else:
			r = mid - 1
	return l

def sort(arr):
	insertion_sort_binary(arr)

def insertion_sort_binary(arr):
	res = [(20, (0, 0))]
	for i in range(0, len(arr)):
		x = arr[i]
		key = x[0]
		pos = binary_search(res, key, 0, i)
		res.insert(pos+1, x)
	return res[1:]

# 测试示例
if __name__ == "__main__":
	# 示例数据：每个元组的第一个元素是整数，第二个元素是另一个元组
	data = [
		(5, ('a', 'b', 'c')),
		(2, ('x', 'y')),
		(8, ('m', 'n', 'o', 'p')),
		(3, ('d', 'e')),
		(10, ('z',)),
		(1, ('f', 'g', 'h')),
		(5, ('same1',)),  # 测试相同键值的情况
		(5, ('same2',))   # 测试相同键值的情况
	]
	
	print("原始列表:")
	for item in data:
		quick_print(item)
	quick_print("")
	
	sorted_data = insertion_sort_binary(data)  # 使用copy避免修改原数组
	
	for item in sorted_data:
		quick_print(item)