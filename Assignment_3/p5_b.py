from p1 import check_primality
import random
import numpy as np

n = int(input("\nEnter the size of the array : "))
arr = np.empty(n) #create array of

print("Randomly filling up the arrays...\n")

for i in range(n): 
    arr[i] = random.randint(0,1000) #random integer generation

print("Printing the array : ", arr)

#----------------------------replacing the even with 0--------------------------------------------------

arr_copy = np.copy(arr)

for i in range(len(arr_copy)):
    if arr_copy[i]%2 == 0:
        arr_copy[i] = 0

print("Printing after replacing the even elements with 0: \n")
print(arr_copy)

#---------------------------extract primes---------------------------------

arr_copy = np.copy(arr)
filtered_prime = filter(check_primality,arr_copy)

print("The prime numbers are : ")
for i in filtered_prime:
    print(i, end=" \t")

print()

#------------------------------------convert 1D to 2d----------------------------------------

arr_copy = np.copy(arr)
arr_copy = arr_copy.reshape([2,-1])

print("Printing the array after converting to a 2D array with 2 rows ")
print(arr_copy, end="\n\n")

#