print("sort and print second last")
list_val = [20, 30, 40, 25, 10]
# sort
list_val.sort()
# second last element
print("The second largest element of the list is:", list_val[-2])



print("------------------------------------------")
print("remove max() element")

list_val = [20, 30, 40, 25, 10]
res_list = set(list_val)
  
#removing the max() element
res_list.remove(max(res_list))
print(max(res_list))



print("------------------------------------------")
print("input elements and find second largest")

list_val = []
# input numbers
num_list = int(input("Enter number of elements in list: "))
for i in range(1, num_list + 1):
	element = int(input("Enter the elements: "))
	list_val.append(element)

list_val.sort()
print("Second largest element is:", list_val[-2])


print("------------------------------------------")
print("traverse the list")
def calc_largest(arr):
	second_largest = arr[0]
	largest_val = arr[0]
	for i in range(len(arr)):
		if arr[i] > largest_val:
			largest_val = arr[i]
	for i in range(len(arr)):
		if arr[i] > second_largest and arr[i] != largest_val:
			second_largest = arr[i]
	return second_largest
print(calc_largest([20, 30, 40, 25, 10]))  

