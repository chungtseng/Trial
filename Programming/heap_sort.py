class Heap(list):
	def left(self,i):
		return 2*i + 1
	def right(self,i):
		return 2*i + 2
	def parent(self,i):
		return int(i/2.0 + 0.5)
	def swap(self, i, j):
		a = self[i]
		self[i] = self[j]
		self[j] = a
		return
	def max_heapify(self,i):
			if 2*i + 1 >= len(self):
				return
			elif 2*i + 1 == len(self) - 1:
				if self[i] < self[self.left(i)]:
					self.swap(i,self.left(i))
				return	
			def max_index(A, i, j):
				if A[i] >= A[j]:
					return i
				else:
					return j
			if self[i] < self[self.left(i)] or self[i] < self[self.right(i)]: 
				m = max_index(self,self.left(i),self.right(i))
				self.swap(i,m)
				self.max_heapify(m)
			elif self[i] < self[self.right(i)]:
				self.swap(i,self.right(i))
				self.max_heapify(self.right(i))
			return
	def build(self):
		for i in xrange(len(self)/2-1,-1,-1):
			self.max_heapify(i)
	
	def heap_sort(self):
		self.build()
		heap = Heap(self[:])
		sorted_list = []
		while heap != []:
			sorted_list.append(heap[0])
			heap.swap(0,len(heap)-1)
			del heap[len(heap)-1]
			heap.max_heapify(0)
		return sorted_list
if __name__ == '__main__':
	a = Heap([1,3,2,5,8,8,-1,30,21])
	print a == [1,3,2,5,8,8,-1,30,21]
	a.build()
	print a
	print a.heap_sort()
	
	