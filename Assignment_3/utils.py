import numpy as np
import random

def check_primality(num): #checks if a number is prime or not
    primality = True
    i = 2
    upperlimit = num//i

    if(num == 2): #2 is prime
        return primality
    
    if(num == 1 or num == 0): #1 and 0 are not prime
        return False

    while(i<=upperlimit): #reduce the upper limit with each iteration for faster convergence
        if(num%i == 0):
            primality = False
            break
        else:
            i += 1
            upperlimit = num//i
    
    return primality

def BS_recursive(arr, ele, low, high): #binary search recursive

    if low <= high:
        mid = (high+low)//2 

        if(arr[mid] == ele): #element found, return the index
            return mid
        
        elif arr[mid] > ele:
            return BS_recursive(arr,ele,low,mid-1) # check the left half
        else:
            return BS_recursive(arr,ele,mid+1,high) #check the right half
    
    else:
        return -1 # return -1 for the not found case

def BS_iterative(arr,ele): #binary search iterative

    low = mid = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high+low)//2 

        if arr[mid] == ele: #element found, return the index
            return mid
        
        elif arr[mid] > ele:  # check the left half
            high = mid-1
        
        else:                    # check the right half
            low = mid+1 
    
    return -1 #return -1 for the not found case

def bubbleSort(arr): #bubble sort
    n = len(arr)
    count = 1
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.

        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            print("Pass number: %d"%count)
            count += 1
            print("Current sorted array: ",arr,end="\n\n")
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def sum_matrices(arr_a, arr_b): #summation of two numpy matrices
    return arr_a+arr_b