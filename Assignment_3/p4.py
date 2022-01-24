import numpy as np

def BS_recursive(arr, ele, low, high):

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

def BS_iterative(arr,ele):

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


if __name__ == "__main__":

    size = int(input("Enter the number of elements in the array... "))
    arr = []
    print("Keep entering the elements...\n")
    for i in range(size):
        element = int(input())
        arr.append(element)
    
    print("\nPrinting the unsorted array...")
    print(arr)

    arr.sort()
    print("Printing the sorted array...")
    print(arr)

    ele = int(input("Enter the element you want to search "))

    print("Enter 1 for searching recursively and 2 for searching iteratively\n")
    choice = int(input())

    if choice == 1:
        id = BS_recursive(arr,ele,0,size-1)
        if id != -1:
            print("Element found in the sorted array at the index : ",id)
        else:
            print("Element not found!!\n")

    else:
        id = BS_iterative(arr,ele)
        if id != -1:
            print("Element found in the sorted array at the index : ",id)
        else:
            print("Element not found!!\n")