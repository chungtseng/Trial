def merge(a, b):
	n = len(a)+len(b)
	merged_list = []
	i = 0
	j = 0
	a.append(float('inf'))
	b.append(float('inf'))
	for k in xrange(n):
		if a[i] < b[j]:
			merged_list.append(a[i])
			i += 1
		else:
			merged_list.append(b[j])
			j += 1
	return merged_list
left = lambda a: a[:len(a)/2]
right = lambda a: a[len(a)/2:]
def merge_sort(a):
	if len(a) <= 1:
		return a
	sorted_left_list = merge_sort(left(a)) 
	sorted_right_list = merge_sort(right(a))
	sorted_list = merge(sorted_left_list,sorted_right_list)
	return sorted_list

if __name__ == '__main__':
	a = [1,2,3,2,5,4,0,-1,9]
	print merge_sort(a)