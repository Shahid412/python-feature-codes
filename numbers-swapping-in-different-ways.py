#1. using temp variable
print ("------------------------------------")
print ("Swap using temp variable")
P = int( input("Please enter value for P: "))
Q = int( input("Please enter value for Q: "))
temp = P
P = Q
Q = temp
print ("The Value of P after swapping: ", P)
print ("The Value of Q after swapping: ", Q)

#2. Using comma operator
print ("------------------------------------")
print ("Swap using comma operator ")
P = int( input("Please enter value for P: "))
Q = int( input("Please enter value for Q: "))
#comma operator 
P, Q = Q, P
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)


#2. Using xor operator
print ("------------------------------------")
print ("Swap using XOR operator ")
P = int( input("Please enter value for P: "))
Q = int( input("Please enter value for Q: "))
# XOR  
P = P ^ Q
Q = P ^ Q
P = P ^ Q
print ("The Value of P after swapping: ", P)
print ("The Value of Q after swapping: ", Q)

#2. Using arithmatic operator
print ("------------------------------------")
print ("Swap using arithmatic operator ")
P = int( input("Please enter value for P: "))
Q = int( input("Please enter value for Q: "))
# arithmatic operators
P = P + Q
Q = P - Q
P = P - Q
print ("The Value of P after swapping: ", P)
print ("The Value of Q after swapping: ", Q)


#2. Using multiplication and division operator
P = int( input("Please enter value for P: "))
Q = int( input("Please enter value for Q: "))
P = P * Q    
Q = P / Q   
P = P / Q  
print ("The Value of P after swapping: ", P)
print ("The Value of Q after swapping: ", Q)
