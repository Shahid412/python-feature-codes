import math
import cmath # complex math

# First method
# Function for finding roots  
def findRoots(a, b, c):
	dis_form = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis_form))
	if dis_form > 0:
		print(" real and different roots ")
		print((-b + sqrt_val) / (2 * a))
		print((-b - sqrt_val) / (2 * a))
	elif dis_form == 0:
		print(" real and same roots")
		print(-b / (2 * a))
	else:
		print("Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val)
		print(- b / (2 * a), " - i", sqrt_val)  


a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
if a == 0:
	print("Input correct quadratic equation")
else:
	findRoots(a, b, c)

# Alternate method
# calculate the discriminant  
print("----------- Alternate method -----------")
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
