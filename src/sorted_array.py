class SortedArray:
	def __init__(self, max_size):
		self.array = []
		self.max_size = max_size

	def add(self, item):
		self.array.append(item)
		self.array.sort(key = lambda x : x[1])
		if len(self.array) > self.max_size:
			self.array.pop()
