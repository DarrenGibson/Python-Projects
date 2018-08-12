#==================================================================
#							     functions
#==================================================================

'''
def getInfo():

	a = int(input('Please enter the first number in the range\nFirst'))
	b = int(input('Please enter the second number in the range\nSecond'))
	return a, b

def loopIt(a, b):
# see if you can use a = 0 here in args
	for i in range(a, b):
		print('i is now {}'.format(i))

getInfo()
loopIt(a, b)
'''

# here are two ways to print hello from a function

# basic function
def hello_func():
	print('hello Function')
	
hello_func()

# with return 
def hello_again():
	return 'hello again'
	
print(hello_again())

# with arguments
def hello_args(greeting):# greeting here is parameter, not arg?!
	return '{} function.'.format(greeting)
	
print(hello_args('hi'))
# with two arguments, 1 already defined if needed
def hello_good(greeting, name = 'nope'):
	return '{} {}, this is function.'.format(greeting, name)
	
print(hello_good('hi','Darren'))





































