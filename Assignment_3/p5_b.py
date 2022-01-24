from utils import check_primality
import random
import numpy as np

n = int(input("\nEnter the size of the array : "))
arr = np.empty(n) #create array of

print("Randomly filling up the arrays...\n")

for i in range(n): 
    arr[i] = random.randint(0,1000) #random integer generation

print("Printing the array : ", arr)

#----------------------------replacing the even with 0--------------------------------------------------
print()
arr_copy = np.copy(arr)

for i in range(len(arr_copy)):
    if arr_copy[i]%2 == 0:
        arr_copy[i] = 0

print("Printing after replacing the even elements with 0: \n")
print(arr_copy)

#---------------------------extract primes---------------------------------
print()
arr_copy = np.copy(arr)
filtered_prime = filter(check_primality,arr_copy)

print("The prime numbers are : ")
for i in filtered_prime:
    print(i, end=" \t")

print()

#------------------------------------convert 1D to 2d----------------------------------------
print()
arr_copy = np.copy(arr)
arr_copy = arr_copy.reshape([2,-1])

print("Printing the array after converting to a 2D array with 2 rows ")
print(arr_copy, end="\n\n")

#-------------------index in the sorted array---------------------------
print()
arr_copy = np.copy(arr)
print("Printing the sorted indices")
print(np.argsort(arr_copy))

#------------------------binary array to boolean array---------------------------
print()
arr = np.array([1,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1])
print("Printing the binary array : ", arr)
print("Printing the array after covertiont to a boolean array : \n", arr.astype(dtype=bool))

#------------------------------spliting array-------------------------------------
print()
arr = np.array([i for i in map(int, input("Enter 10 elements : ").split(' '))])
print("Printing the array : ", arr)

a = arr[:2]
b = arr[2:4]
c = arr[4:]

print("Printing the splitted arrays : ")
print(a)
print(b)
print(c)
print()
