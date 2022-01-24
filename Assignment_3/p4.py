import numpy as np
from utils import BS_iterative, BS_recursive


if __name__ == "__main__":

    size = int(input("Enter the number of elements in the array... "))
    arr = []
    print("Keep entering the elements...\n")
    for i in range(size): #taking input of array
        element = int(input())
        arr.append(element)
    
    print("\nPrinting the unsorted array...")
    print(arr)

    arr.sort() #sort the array for binary search
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