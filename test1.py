# -*- coding: cp1252 -*-
# python script #

name = 'fabio'
print('hello ' + name + ','),

seriesLen = int(raw_input("Please enter a number: "))

print "you entered", seriesLen

print("here is a Fibonacci series up to " + str(seriesLen) + ": ")

a = 0
b = 1
numList = []
print('printing numbers as i calculate them')
while b <= int(seriesLen):
	print b,
	a, b = b, a+b
	# while printing out the numbers, i'll also build a list
	numList.append(a)
	
 

print('\nprinting list')
print(numList)
	 
	 
print('\ndone')
