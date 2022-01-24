import numpy as np
from utils import sum_matrices

if __name__ == "__main__":

    print("\nEnter the dimensions of the matrices...\n")
    r = int(input("Enter the number of rows "))
    c = int(input("Enter the number of columns "))

    arr_a = np.empty((r,c))
    arr_b = np.empty((r,c))

    print("\nEnter the elements for the first matrix\n")
    for i in range(r):
        for j in range(c):
            print("Enter the element of row %d and column %d "%(i,j))
            arr_a[i,j] = int(input())

    print("\nEnter the elements for the second matrix\n")
    for i in range(r):
        for j in range(c):
            print("Enter the element of row %d and column %d "%(i,j))
            arr_b[i,j] = int(input())
    
    print(arr_a,end="\n\n")
    print(arr_b,end="\n\n")

    arr_sum = sum_matrices(arr_a,arr_b)
    print("Print the sum of two matrices : \n")
    print(arr_sum)