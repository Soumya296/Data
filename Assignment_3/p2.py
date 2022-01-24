from utils import bubbleSort

if __name__ == "__main__":

    size = int(input("Enter the number of elements in the array... "))
    arr = []
    print("Keep entering the elements...\n")
    for i in range(size):
        element = int(input())
        arr.append(element)
    
    print("\nPrinting the unsorted array...")
    print(arr)

    bubbleSort(arr)
    print("Printing the sorted array...")
    print(arr, end="\n\n")