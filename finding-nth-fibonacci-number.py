def Fibonacci_Series(n):
	if n < 0:
		print("Oops! Incorrect input")
	# First Fibonacci number is 0
	elif n == 0:
		return (0)   
    # Second Fibonacci number is 1
	elif n == 1:
		return (1)
	else:
		return (Fibonacci_Series(n - 1) + Fibonacci_Series(n - 2))   
# printing the 12th element of the Fibonacci Series  
n= int(input("please input 'n': "))
print(n,"th Element of the Fibonacci Series : ", Fibonacci_Series(n))