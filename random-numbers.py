import random

n = random.random()
print(n)

#using a range

n = random.randint(0,50)
print(n)


#multuiple random numbers using loop
rand_list = []
for i in range(0,10):
    n = random.randint(1,50)
    rand_list.append(n)
print(rand_list)


#generate a list of random numbers
random_list = random.sample(range(10, 40), 6) #generate 6 numbers
print(random_list)