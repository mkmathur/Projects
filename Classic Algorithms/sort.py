def merge_sort(arr):
	if(len(arr) <= 1):
		return arr
	mid = int(len(arr) / 2)
	left = arr[:mid]
	right = arr[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left, right)

def merge(a1, a2):
	result = []
	p1 = 0
	p2 = 0
	while p1 < len(a1) and p2 < len(a2):
		if(a1[p1] < a2[p2]):
			result.append(a1[p1])
			p1 += 1
		else:
			result.append(a2[p2])
			p2 += 1
	while p2 < len(a2):
		result.append(a2[p2])
		p2 += 1
	while p1 < len(a1):
		result.append(a1[p1])
		p1 += 1
	return result
