import numpy as np
import random

n = int(input("\nEnter the size of the arrays : "))

arr_a = np.empty(n) #create array of dimension n
arr_b = np.empty_like(arr_a) #create a array of same dimension of arr_a

print("Randomly filling up the arrays...\n")

for i in range(n): 
    arr_a[i] = random.randint(0,1000) #random integer generation

print("Printing the first array : ", arr_a)

for i in range(n):
    arr_b[i] = random.randint(0,1000) #random integer generation

print("Printing the second array : ", arr_b)

print("Displaying the elements of the first array whose corresponding elements in the second array is less or equal\n")

for i in range(n):
    if arr_b[i] <= arr_a[i]:
        print("Index : %d element of array 1: %d element of array 2: %d"%(i,arr_a[i],arr_b[i]))

print()