
# python script #



name = 'fabio'
print('hello ' + name + ','),

seriesLen = int(input("Please enter a number: "))

print ("you entered", seriesLen)

print("here is a Fibonacci series up to " + str(seriesLen) + ": ")

# initialisation of variables
a = 0
b = 1

numList = []
print('printing numbers as i calculate them')
while b <= int(seriesLen):
	print (b)
	a, b = b, a+b
	# while printing out the numbers, i'll also build a list
	numList.append(a)
	

# printing the final list
print('\nprinting list')
print(numList)
	 
# end of script	 
print('\ndone')
