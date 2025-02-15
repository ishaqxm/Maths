while True:
	n=int(input('Enter a natural number: '))
	for i in range(1,2*n,2):
		print(i,end=' + ')
		#
	def odd(n):
		if n == 1:
			return 1
		else:
			return (n*2 - 1) + odd(n - 1)
	print('\b\b=',odd(n),f'= ({n})²\n')