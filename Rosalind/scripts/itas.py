m = 1355
n = 1932
def comb_numb(n,k):
	result = 1
	if k > n/2:
		k = n-k
	for i in xrange(n-k+1, n+1):
		result *= i
	for i in xrange(1,k+1):
		result /= i
	return result
result = 0
for i in xrange(m,n+1):
	result += comb_numb(n,i)
print (result)%10**6