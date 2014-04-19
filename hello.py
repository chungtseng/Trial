class hello(object):
	def __init__(self,words):
		self.words = words
	def exp(self):
		print self.words

if __name__ == '__main__':
	a = hello('naive')
	a.exp()
